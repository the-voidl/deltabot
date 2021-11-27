import simplebot


@simplebot.filter
def cryptWatch(message, replies):
    """Cryptwatch: I look for law and order on this dark coast!"""
    if not message.is_encrypted():
        replies.add(text="⚠️⚠️⚠️ This message is not encrypted ⚠️⚠️⚠️", quote=message)


@simplebot.command
def kick(bot, message, payload, replies):
    """Kick users from the group:
    Either swipe to replay and send '/kick' to kick the sender
    or
    Send '/kick mail@example.com' to kick this user
    """
    if not message.chat.is_group():
        replies.add(text="You must send me this command in a group.")

    else:
        myself = bot.account.get_config("addr")

        if message.quoted_text != None:
            acc = message.quote.get_sender_contact().addr
        elif len(payload) > 4:
            acc = payload
        else:
            replies.add(text="""Good pilgrim, you do wrong you hand too much,
Which mannerly devotion shows in this;
For saints have hands that pilgrims’ hands do touch,
And palm to palm is holy palmers’ kiss.""", sender="William Shakespeare", quote=message)
            return

        if acc == myself:
            replies.add(text="""Ha! Ha! What ought I to do?
Ban myself off this grateful union? What a charlatan you are...""", quote=message)
        else:
            try:
                for member in message.chat.get_contacts():
                    if member.addr == acc:
                        message.chat.remove_contact(acc)
                        return
                    else:
                        replies.add("{} not in this group".format(acc))
            except:
                replies.add(text="Could not remove {}".format(acc))
