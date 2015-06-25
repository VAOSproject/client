#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import wikipedia
import os, re
import wolframalpha
import goslate
import profile

gs = goslate.Goslate()

def wiki_info(language, content):
    wikipedia.set_lang(language)
    return re.sub(r'\(.*?\)', '', wikipedia.summary(content, sentences=2))

def wolfram(language, api, answer):
    answer_translated= gs.translate(answer, "en")#We need to translate this to english for Wolfram to understand it
    client = wolframalpha.Client("T8576G-3UU5PE5U5R")
    res = client.query(answer_translated)
    if len(res.pods) > 0:
        texts = ""
        pod = res.pods[1]
        if pod.text:
            texts = gs.translate(pod.text, language)
        else:
            texts = "No puedo responder a eso"
        # to skip ascii character in case of error
        texts = texts.encode('ascii', 'ignore')
        return re.sub(r'\(.*?\)', '',texts)
    else:
        return "Lo siento, no estoy segura."

def wolfram_english(api, answer):
    client = wolframalpha.Client(api)
    res = client.query(answer)
    if len(res.pods) > 0:
        texts = ""
        pod = res.pods[1]
        if pod.text:
            texts = pod.text
        else:
            texts = "I have no answer for that"
        # to skip ascii character in case of error
        texts = texts.encode('ascii', 'ignore')
        return re.sub(r'\(.*?\)', '',texts)
    else:
        return "Sorry, I am not sure."

def knowledge(language, api, phrase, ascii_phrase):
    if "quien" in ascii_phrase or "que" in ascii_phrase:
        info=' '.join(phrase.split()[2:]) #We delete the two first words (who is/quien es etc)
        return wiki_info(language, info)
    else:
        return wolfram(language, api, phrase)
