#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import urllib2
import json
from pushbullet import Pushbullet
import profile

def sendNotification_Pushetta(message):
	data = {
		"body" : message,
		"message_type" : "text/plain"
	}
 
	req = urllib2.Request('http://api.pushetta.com/api/pushes/{0}/'.format(profile.pushetta_channel))
	req.add_header('Content-Type', 'application/json')
	req.add_header('Authorization', 'Token {0}'.format(profile.pushetta_api))

	response = urllib2.urlopen(req, json.dumps(data))

def sendNotification_Pushbullet(message):
    pb = Pushbullet(profile.pushbullet_api)
    push = pb.push_note("VAOS", message)

def sendNotification(message):
	if profile.notification_service == "PUSHBULLET":
		sendNotification_Pushbullet(message)
	elif profile.notification_service == "PUSHETTA":
	    sendNotification_Pushetta(message)