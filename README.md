Having fun with DeltaChat
---

This repository collects nice scripts ("plugins") for the [SimpleBot](https://github.com/simplebot-org/simplebot) bot for [DeltaChat](https://delta.chat/).

DeltaChat is a nice e-mail based messenger that uses autocrypt.
Even when you do not own your own mailserver, this ensures that all your messages get encrypted by GPG and ar fully under your control.
Actually they are only encrypted if the other side also uses Autocrypt.

## Dependencies
To use these scripts you need:
- DeltaChat binding for python `pip install deltachat`
- SimpleBot `pip install simplebot`

Some plugins use python modules:
- bot-count: `pip install randfacts wikipedia`


## Getting started
SimpleBot needs to be initialized with mail accounts. It uses IMAP and SMTP. I use an `.env` file to store my credentials like following:
```
#.env
ADDR="deltabot@example.com"
PASSWORD="SuPeR_SaFe_PaSsWoRd"
```

1. Add the account(s)
2. `cd` into the directory where you stored the .py plugin files. A plugin is identified by it's file name.
3. Add the plugin(s) to your account(s)
4. Start the service and enjoy!

```
$ cd deltabot && ls deltabot
> myFancyPlugin.py
$ source .env
$ simplebot init "$ADDR" "$PASSWORD"
$ simplebot -a deltabot@example.com plugin -a myFancyPlugin.py
$ simplebot -a deltabot@example.com serve &>/dev/null &
```
