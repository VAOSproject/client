#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#Import our own modules
import profile
from tts import tts
from modules import music
from modules import knowledge
from modules import translator
from modules import twitter
from modules import gag

def brain(phrase, ascii_phrase):
        phrase=phrase
        ascii_phrase=ascii_phrase
        if "como se dice" in phrase:
            text= ' '.join(phrase.split()[3:-2])
            language= ascii_phrase.split()[-1]
            tts.tts_translator(translator.translate(text, language), language) #Después de las 3 primeras palabras (como se dice) hasta la última, el idioma
        elif "eres" in phrase:
            return "Mi nombre es VAOS, soy un asistente personal de codigo abierto capaz de reproducir canciones, hacer twits, deletrear palabras, contar chistes, buscar informacion sobre cualquier famoso, hacer operaciones matematicas y mucho mas."
        elif "musica" in ascii_phrase or "escuchar" in ascii_phrase:
            music.music(phrase)
        elif "canta" in ascii_phrase or "cantame" in ascii_phrase or "estoy" in ascii_phrase or "chiste" in ascii_phrase:
            return profile.tts, gag.gag(phrase)
        elif "twitter" in phrase or "twittear" in phrase:
        	return twitter.status(phrase)
        elif "apagar" in ascii_phrase:
        	auto_recognition=False
        elif "Gloria" in ascii_phrase or "gloria" in ascii_phrase:
        	music.play("gloria.mp3")
        elif "deletrear" in phrase:
            print list(ascii_phrase.split()[-1])
            return list(ascii_phrase.split()[-1])
        elif phrase == "Error":
            return "La voz no se ha podido reconocer correctamente"
        else:
            return knowledge.knowledge(profile.language, profile.wolfram_api, phrase, ascii_phrase)