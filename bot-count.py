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
    Well, not every number. It just responds with a probability of 30% to let other users a chance.
    And it adds a bit of functionality to bring more fun to the group.
    You can browse my code here: https://github.com/the-voidl/deltabot/blob/master/bot-count.py
    """
    startAt = 1000
    propability = 30

    number = int(findNumber(message.text))
    if number != 0 and number > startAt and random.randrange(1,101) <= propability:
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
    if isLiquorNumber(number):
        return "🎉🎊 {} 🎊🎉".format(number)
    elif getPortDescription(number):
        return "Port {}: {}".format(number, getPortDescription(number))
    else:
        rand = random.randrange(1,7)

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

def isLiquorNumber(number):
    ret = True
    numberString = str(number)
    if len(numberString) > 1:
        if numberString[0] == numberString[1]:
            return isLiquorNumber(numberString[1:])
        else:
            ret = False
    return ret

def getPortDescription(number):
    ports = {
    110:	"Post Office Protocol version 3",
    111:	"Remote Procedure Call (RPC) Protocol for remote command execution, used by Network Filesystem (NFS)",
    113:	"Authentication and Ident protocols",
    115:	"Secure File Transfer Protocol (SFTP) services",
    117:	"Unix-to-Unix Copy Protocol (UUCP) Path services",
    119:	"Network News Transfer Protocol (NNTP) for the USENET discussion system",
    123:	"Network Time Protocol (NTP)",
    137:	"NETBIOS Name Service used in Red Hat Enterprise Linux by Samba",
    143:	"Internet Message Access Protocol (IMAP)",
    161:	"Simple Network Management Protocol (SNMP)",
    162:	"Traps for SNMP",
    163:	"Common Management Information Protocol (CMIP)",
    164:	"Common Management Information Protocol (CMIP)",
    174:	"MAILQ email transport queue",
    177:	"X Display Manager Control Protocol (XDMCP)",
    178:	"NeXTStep window server",
    179:	"Border Gateway Protocol",
    191:	"Prospero distributed filesystem services",
    194:	"Internet Relay Chat (IRC)",
    199:	"SNMP UNIX Multiplexer",
    201:	"AppleTalk routing",
    202:	"AppleTalk name binding",
    204:	"AppleTalk echo",
    206:	"AppleTalk zone information",
    209:	"Quick Mail Transfer Protocol (QMTP)",
    213:	"Internetwork Packet Exchange (IPX), a datagram protocol commonly used in Novell Netware environments",
    220:	"Internet Message Access Protocol version 3",
    363:	"RSVP Tunnel",
    372:	"UNIX LISTSERV",
    389:	"Lightweight Directory Access Protocol (LDAP)",
    427:	"Service Location Protocol (SLP)",
    434:	"Mobile Internet Protocol (IP) agent",
    435:	"Mobile Internet Protocol (IP) manager",
    443:	"Secure Hypertext Transfer Protocol (HTTP)",
    444:	"Simple Network Paging Protocol",
    445:	"Server Message Block (SMB) over TCP/IP",
    464:	"Kerberos password and key changing services",
    487:	"Simple Asynchronous File Transfer (SAFT) protocol",
    500:	"Internet Security Association and Key Management Protocol (ISAKMP)",
    535:	"Internet Inter-Orb Protocol (IIOP)",
    538:	"GNUstep Distributed Objects Mapper (GDOMAP)",
    546:	"Dynamic Host Configuration Protocol (DHCP) version 6 client",
    547:	"Dynamic Host Configuration Protocol (DHCP) version 6 Service",
    563:	"Network News Transport Protocol over Secure Sockets Layer (NNTPS)",
    565:	"whoami user ID listing",
    587:	"Mail Message Submission Agent (MSA)",
    612:	"HyperMedia Management Protocol (HMMP) Indication / DQS",
    631:	"Internet Printing Protocol (IPP)",
    636:	"Lightweight Directory Access Protocol over Secure Sockets Layer (LDAPS)",
    694:	"Heartbeat services for High-Availability Clusters",
    765:	"Network Dictionary",
    767:	"Network Phonebook",
    873:	"rsync file transfer services",
    992:	"Telnet over Secure Sockets Layer (TelnetS)",
    993:	"Internet Message Access Protocol over Secure Sockets Layer (IMAPS)",
    994:	"Internet Relay Chat over Secure Sockets Layer (IRCS)",
    995:	"Post Office Protocol version 3 over Secure Sockets Layer (POP3S)",
    1080:   "SOCKS network application proxy services",
    1433:   "Microsoft SQL Server",
    1512 	"Microsoft Windows Internet Name Server",
    1649:   "Kermit file transfer and management service",
    4321:   "Remote Whois (rwhois) service",
    6000:   "X Window System services",
    10080:	"Advanced Maryland Automatic Network Disk Archiver (Amanda) backup services",
    11371:	"Pretty Good Privacy (PGP) / GNU Privacy Guard (GPG) public keyserver",
    11720:	"H.323 Call Signal Alternate",
    13720:	"NetBackup Request Daemon (bprd)",
    13721:	"NetBackup Database Manager (bpdbm)",
    13722:	"Veritas NetBackup Java / Microsoft Visual C++ (MSVC) protocol",
    13724:	"network utility",
    13782:	"NetBackup",
    13783:	"VOPIE authentication daemon",
    22273:	"Kana/Kanji conversion system[c]",
    26000:	"Quake (and related) multi-player game servers",
    26208:	"Wnn6 Kana/Kanji server",
    33434:	"traceroute"
    }
    return ports.get(number, "")


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
        
