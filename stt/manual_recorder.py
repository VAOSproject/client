import pyaudio
import wave
import time
import stt
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)

def listen(language):
    CHUNK = 1024 
    FORMAT = pyaudio.paInt16 
    CHANNELS = 1 
    RATE = 16000 

    p = pyaudio.PyAudio()
    
    while GPIO.input(23)==False:
    	continue

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK) #buffer

    print("* recording")

    frames = []

    while GPIO.input(23):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")
    filename='output_'+str(int(time.time()))+'.wav'

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return stt.stt_google_wav(filename, language)