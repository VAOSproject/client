#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import random
import pygame
import os
import os.path
import glob
import fnmatch, re
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
pygame.mixer.init()

#FUNCTIONS

def button(play):
    if play:
        pygame.mixer.music.pause()
        print "Pause"
    elif play == False:
        pygame.mixer.music.unpause()
        print "Play"

def control_music():
    while GPIO.input(23) == False:
        continue
    button(True)
    time.sleep(0.3)
    while GPIO.input(23) == False:
        continue
    button(False)
    time.sleep(0.3)

def play(file): #PLAY A SOUND
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def custom_song(name):
    pattern = re.compile(fnmatch.translate("*"+name + "*.mp3"), re.IGNORECASE)
    directory = './music/'
    for name in os.listdir(directory):
        if pattern.match(name):
            print(os.path.join(directory, name))
            pygame.mixer.music.load(os.path.join(directory, name))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                control_music()

def random_music():
	DIR="music/"
	music = filter(lambda x: x.lower().endswith("mp3"),os.listdir(DIR))
	music = list(music)
	while 1:
	    song = random.choice(music)
	    pygame.mixer.music.load(os.path.join(DIR,song))
	    pygame.mixer.music.play()
	    while pygame.mixer.music.get_busy() == True:
	        control_music()

def music(phrase):
    if "aleatoria" in phrase or "musica" in phrase:
        random_music()
    elif "escuchar" in phrase:
        song = ' '.join(phrase.split()[2:]) #Just the name of the song
    	print song
        custom_song(song)
