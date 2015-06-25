#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import speech_recognition as sr

def stt_google_wav(file, language):
    r = sr.Recognizer( language , key = "AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
    with sr.WavFile(file) as source:            
        audio = r.record(source)
        try:            
            return r.recognize(audio)
        except LookupError:
            return "Error"
        except IndexError:
            return "Error"
        except KeyError:  
            return "Error"

