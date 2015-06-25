#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import subprocess
import pyttsx
import unicodedata

def remove_tildes(text): #Used for google and festival tts
    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(text)) if unicodedata.category(c) != 'Mn'))
    return s.decode()

def talk_google(text): #Google tts (Online)
    ascii_text=remove_tildes(text) #As python only works with ascii characteres, we have to do this if we want the rest of the things to work properly
    subprocess.Popen("./tts/speech.sh" + " " + ascii_text, shell=True)

def talk_pyttsx(text): #pyttsx (Offline)
    engine = pyttsx.init()
    engine.setProperty('voice', "spanish")
    engine.say(text)
    engine.runAndWait()

def talk_festival(text): #Festival (Offline, probably the best)
    ascii_text=remove_tildes(text)
    subprocess.call('echo '+ascii_text+'|festival --tts', shell=True)

def tts_translator(phrase, language): #We use google tts for translations, and we don't use the .sh because the translations shoud be short
    if language == "ingles":
        language="en"
    elif language == "portugues":
        language="pt"
    elif language == "aleman":
        language="nl"
    elif language == "italiano":
        language="it"
    elif language == "frances":
        language="fr"
    elif language == "spanish":
        language="es"
    googleSpeechURL = "http://translate.google.com/translate_tts?tl="+ language +"&q=" + phrase
    subprocess.call(["mplayer",googleSpeechURL], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def talk(tts, text):
    if tts=="GOOGLE":
        talk_google(text)
    elif tts=="PYTTSX":
        talk_pyttsx(text)
    elif tts=="FESTIVAL":
        talk_festival(text)
