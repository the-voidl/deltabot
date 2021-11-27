import simplebot

@simplebot.filter
def cryptWatch(message, replies):
    """Cryptwatch: I look for law and order on this coast!"""
    if not message.is_encrypted():
        replies.add(text="⚠️⚠️⚠️ This message is not encrypted ⚠️⚠️⚠️", quote=message)
