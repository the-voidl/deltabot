import simplebot
import re
import random
import time

@simplebot.filter
def beHappy(message, replies):
    """BeHappy: Don't worry be happy!"""
    if not message.is_text():
        return

    exp = r"[😑😐😒😔😕😟🙁☹️😢😥😰😭😢]|(:-?[\(/])"
    random.seed(time.time())

    if re.search(exp, message.text) != None :
        rand = random.randrange(1,6)
        if rand == 1:
            sendPussy(message, replies)
        elif rand == 2:
            sendGeileSau(message, replies)
        elif rand == 3:
            sendSong(message, replies)
        elif rand >= 4:
            sendCables(message, replies)

def sendSong(message, replies):
    random.seed(time.localtime().tm_sec)
    rand = random.randrange(1,4)
    songs = {
    1: "Listen to this: https://www.youtube.com/watch?v=L3HQMbQAWRc", # Bob Marley
    2: "Ooh Eeh Ooh Ah Aaahh\nhttps://www.youtube.com/watch?v=cmjrTcYMqBM", # Davis Seville
    3: "Other people even want to fuck dogs... Or pirates xD https://www.youtube.com/watch?v=RvaMi5CT3Xg" # Blink 182
    }
    reply = "Not so mad, {}!\n{}".format(message.get_sender_contact().name, songs.get(rand))
    replies.add(text=reply, quote=message)

def sendCables(message, replies):
    reply = "Hey {}, here are some sexy cables to cheer you up :)".format(message.get_sender_contact().name)
    random.seed(time.localtime().tm_sec)
    rand = random.randrange(0,5)
    fileName = "images/cables{}.jpg".format(rand)
    replies.add(text=reply, filename=fileName, quote=message)

def sendPussy(message, replies):
    reply = "Don't be sad, {}!\nHere is a cute chick with a hairy pussy to brighten you up :)".format(message.get_sender_contact().name)
    replies.add(text=reply, filename="images/pussy.png", quote=message)

def sendGeileSau(message, replies):
    reply = "{}! Nicht böse sein!\nUm dich aufzuheitern hab ich hier eine geile Sau in Lackstiefeln für dich ^.^".format(message.get_sender_contact().name)
    replies.add(text=reply, filename="images/geilesau.jpg", quote=message)
