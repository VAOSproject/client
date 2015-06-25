#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import random

def file_len(nfile):
    with open(nfile) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def joke():
    number= random.randrange(file_len("modules/gags/jokes.py"))
    f=open('modules/gags/jokes.py')
    lines=f.readlines()
    print (lines[number])
    return lines[number]

def song():
    number= random.randrange(file_len("modules/gags/songs.py"))
    f=open('modules/gags/songs.py')
    lines=f.readlines()
    print (lines[number])
    return lines[number]

def appearance():
    number= random.randrange(file_len("modules/gags/appearance.py"))
    f=open('modules/gags/appearance.py')
    lines=f.readlines()
    return lines[number]

def gag(phrase):
    if "cantame" in phrase or "canta" in phrase:
        return song()
    elif "estoy" in phrase:
        return appearance()
    elif "chiste" in phrase:
        return joke()