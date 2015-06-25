#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import pygame
import time
import unicodedata
import glob
import os, shutil
pygame.mixer.init()
#Import our own modules
import profile
import brain
import notification
from tts import tts
from stt import stt
from modules import music

def remove_tildes(text):
    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(text)) if unicodedata.category(c) != 'Mn'))
    return s.decode()

def clean_files():
    while len(glob.glob("./"+"*.wav")) > 0: #Delete all the voice files
        os.remove(glob.glob("./"+"*.wav")[0])

def main(phrase):
    ascii_phrase= remove_tildes(phrase) #As python only works with ascii characteres, we have to do this if we want the rest of the things to work properly
    
    print ascii_phrase

    result= brain.brain(phrase, ascii_phrase)

    if result: #Some functions doesn't return anything
        print result
        tts.talk(profile.tts, result)
        notification.sendNotification(result)

print "Program started"
music.play("sounds/started.mp3")
notification.sendNotification("Started")

#ALWAYS LISTENING MODE
while profile.auto_recognition==True:
    from stt import auto_recorder
    while profile.name not in auto_recorder.passive_listen(profile.language): #Look for the name
        clean_files()
    music.play("sounds/name.wav") #The name has been detected

    phrase = auto_recorder.listen(profile.language)
    print (phrase)
    main(phrase)

#MANUAL MODE (BUTTON)
while profile.auto_recognition==False:
    from stt import manual_recorder
    
    phrase = manual_recorder.listen(profile.language)
    print (phrase)
    main(phrase)

    clean_files()
    