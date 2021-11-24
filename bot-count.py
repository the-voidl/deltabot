import simplebot
import re
import random
import randfacts
import wikipedia


@simplebot.filter
def count(message, replies):
    """
    This plugin is designed to take part in a bigger thing.
    This bigger thing is called a group.
    Actually it just counts up every number it receives.
    Actually not every number. It just responds with a probability of 33% to let other users a chance.
    And it adds a bit of functionality to bring fun to the group.
    You can browse my code here: https://github.com/the-voidl/deltabot/blob/master/bot-count.py
    """
    startAt = 1000
    number = int(findNumber(message.text))
    if number != 0 and number > startAt and random.randrange(1,4) == 2:
        nextNumber = number + 1
        reply = getReply(nextNumber)
        replies.add(text=reply)

def findNumber(message):
    """
    RegEx search for any number in the received message.
    @returns The only number in the text or 0 if none ore more numbers found
    """
    found = re.findall(r'\d+', message)
    print(found)
    if len(found) == 1:
        return found[0]
    else:
        return 0

def getReply(number):
    """
    Main logic for defining a reply.
    Randomly chooses a string from `switcher` or an error string.
    """
    rand = random.randrange(1,7)
    rand = 5
    switcher={
    1: getWikiPerID(number),
    2: "My time has come!\n**{}**".format(number),
    3: "Random fact no.{}:\n\n{}".format(number, randfacts.get_fact()),
    4: "{}".format(number),
    5: getAsciiNumber(number)
    }

    return switcher.get(rand, "Huston, we have a problem. ERR_NO: _{}_".format(number))

#
# --- Additional functionalities for more fun ---
#

def getWikiPerID(number):
    try:
        page = wikipedia.page(pageid=number)
        return "Wikipedia Page #{}:\n{}".format(number, page.summary)
    except:
        return "There is no Wikipedia page with ID#{} 🙁".format(number)

def getAsciiNumber(number):
    roundy = [ "⓪", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨ " ]
    corny = [ "0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"  ]
    numbers = [ "" ]
    if random.randrange(1,3) == 1:
        numbers = roundy
    else:
        numbers = corny

    numberString = ""
    for c in str(number):
        numberString += numbers[int(c)]
    return numberString


def getWiki(number):
    """Currently not used 'cause wikipedia API has a bug"""
    try:
        #summary = wikipedia.summary(query="{}".format(number), auto_suggest=False)
        summary = wikipedia.summary(query="{}".format(number))
        if summary.contains(str(number)):
            return fact
        else:
            raise RuntimeError()
    except:
        return "{}".format(number)
        
