#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import goslate
gs = goslate.Goslate()

ingles="en"
spanish="es"
portugues="pt"
aleman="nl"
italiano="it"
frances="fr"

def translate(text, language):
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
	return gs.translate(text, language)