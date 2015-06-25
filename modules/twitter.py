#!/usr/bin/env python
import tweepy
 
#Coloca dentro de las comillas tus claves...
CONSUMER_KEY = '44Wnz8irkDysWAWhswKdo7PSH' 
CONSUMER_SECRET = '5zy7Qjw7qSQ2LDNLMRCLaBPJS9C0UCTVwnaULyrLbEiJ708bJx'
ACCESS_KEY = '1352275296-gYgr5zrEieIONzI0scePkJYQcwCPHqenSxDp9Zt'
ACCESS_SECRET = 'DwI1utCbdZc5u3LJzI6u2jr4dQynk43tC2PYRajeGYR0o'
 
#En esta parte nos identifica para poder realizar operaciones
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
 
#update_status('mensaje' o variable) es para actualizar nuestro estado
def status(phrase):
    status= ' '.join(phrase.split()[1:])
    if len(status) > 140:
    	return "No se puede twittear. El texto es demasiado largo"
    else:
        api = tweepy.API(auth)
        api.update_status(status=status)
        return (status +" twiteado correctamente")