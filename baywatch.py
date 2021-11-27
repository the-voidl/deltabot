import simplebot
import re
import random
import io
import time
from urllib.request import urlopen

@simplebot.filter
def cryptWatch(message, replies):
    """Baywatch: I look for law and order on this beach!"""
    if not message.is_encrypted():
        replies.add(text="⚠️⚠️⚠️ This message is not encrypted ⚠️⚠️⚠️", quote=message)

@simplebot.filter
def beHappy(message, replies):
    """BeHappy: Don't worry be happy!"""
    if not message.is_text():
        return

    exp = r"[😑😐😒😔😕😟🙁☹️]|(:\()"
    random.seed(time.time())

    if re.search(exp, message.text) != None :
        rand = random.randrange(1,7)
        if rand == 1:
            sendPussy(message, replies)
        elif rand == 2:
            sendGeileSau(message, replies)
        elif rand == 3:
            replies.add("Not so mad! Listen to this: https://www.youtube.com/watch?v=L3HQMbQAWRc", quote=message)
        elif rand >= 4:
            sendCables(message, replies)

def sendCables(message, replies):
    reply = """Hey {}, here are some sexy cables to cheer you up :)""".format(message.get_sender_contact().name)
    random.seed(time.localtime().tm_sec)
    rand = random.randrange(0,5)
    fileName = "images/cables{}.jpg".format(rand)
    replies.add(text=reply, filename=fileName, quote=message)

def sendPussy(message, replies):
    reply = """Don't be sad, {}!\nHere is a cute chick with a hairy pussy to brighten you up :)""".format(message.get_sender_contact().name)
    replies.add(text=reply, filename="images/pussy.png", quote=message)

def sendGeileSau(message, replies):
    reply = """{}! Nicht böse sein!\nUm dich aufzuheitern hab ich hier eine geile Sau in Lackstiefeln für dich ^.^""".format(message.get_sender_contact().name)
    replies.add(text=reply, filename="images/geilesau.jpg", quote=message)
