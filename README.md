<p align="center"><a href="https://t.me/fridayot"><img src="https://telegra.ph/file/22535f8051a58af113586.jpg" width="5000"></a></p> 
<h1 align="center"><b>FRIDAY-USERBOT 🇮🇳 </b></h1>
<h4 align="center">A Powerful, Smart And Simple Userbot In Pyrogram.</h4>


## Support 🚑
<a href="https://t.me/FridaySupportOfficial"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a>
<a href="https://t.me/fridayOT"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>

## Inspiration & Credits
* [Userge-X](https://github.com/code-rgb/USERGE-X/contributors)
* [Userge](https://github.com/UsergeTeam/Userge)
* [Pokurt](https://github.com/UsergeTeam/Pokurt)
* [Pyrogram](https://github.com/pyrogram/pyrogram/contributors)

## Code Owners
* [Chsaiujwal](https://github.com/chsaiujwal)
* [Aditya](https://github.com/Aditya-XD)
* [Lakhac](https://github.com/Lakhac)
* [InukaAsith](https://github.com/InukaAsith)
* [SHRE-YANSH](https://github.com/SHRE-YANSH)

# String Session - Pyrogram 🖱
### Repl 🧨
[![Run on Repl.it](https://repl.it/badge/github/STARKGANG/friday)](https://replit.com/@MIDHUNKMKM/StringGen)
### Locally 🏆
```
$ git clone https://github.com/DevsExpo/FridayUserbot
$ cd FridayUserBot
$ python(3) string_gen.py
```

# Hosting 🖥

### Deploying To Heroku / Railway ⚙

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/DevsExpo/FridayUserBot)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2FDevsExpo%2FFridayUserBot&envs=API_HASH%2CAPI_ID%2CBOT_TOKEN%2CLOG_GRP%2CMONGO_DB%2CSTRINGSESSION%2CTZ&optionalEnvs=BOT_TOKEN%2CCOMMAND_HANDLER%2CUPSTREAM_REPO&API_HASHDesc=Get+this+value+from+my.telegram.org%21+Please+do+not+steal&API_IDDesc=Get+this+value+from+my.telegram.org%21+Please+do+not+steal&BOT_TOKENDesc=Your+Bot+Token+Obtained+From+%40BotFather.+This+is+Not+Important&COMMAND_HANDLERDesc=Your+Command+Handler.&LOAD_UNOFFICIAL_PLUGINSDesc=Do+You+Wish+To+Load+X-Tra+Plugins%3F&LOG_GRPDesc=A+Group+ID+Where+You+Want+To+Log+Important+Logs.&MONGO_DBDesc=Create+A+Database+In+Mongodb+And+Get+URL.+Make+Sure+To+Enter+Correct+URL%21&STRINGSESSIONDesc=String+Session%2C+Run+string_gen.py+to+get+String+Session.&TZDesc=Your+Time+Zone&LOAD_UNOFFICIAL_PLUGINSDefault=True&TZDefault=Asia%2FKolkata)
## !Do not deploy on railway else your account will be suspended.

### Self-hosting (For Devs) ⚔
```sh
# Install Git First // (Else You Can Download And Upload to Your Local Server)
$ git clone https://github.com/DevsExpo/FridayUserBot
# Open Git Cloned File
$ cd FridayUserBot
# Install All Requirements 
$ pip3 install -r requirements.txt
# Create local.env with variables as given below
# Start Bot 
$ python3 -m main_startup
```


### Mandatory Configs 📒
```
[+] Make Sure You Add All These Mandatory Vars. 
    [-] API_ID:   You can get this value from https://my.telegram.org
    [-] API_HASH :   You can get this value from https://my.telegram.org
    [-] STRINGSESSION : Your String Session, You can get this From Repl or BY running String_Gen File Locally
    [-] MONGO_DB : Your Mongo DB DataBase Url. 
    [-] LOG_GRP: Your Log Group/Channel Chat ID. This is Very Important and Some Modules Will Not Work Well Without This!
[+] The fridayUserbot will not work without setting the mandatory vars.
```

# Examples - Plugins 👊

### Plugins 🔧

```python3
from main_startup.core.decorators import friday_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply

@friday_on_cmd(['helloworld'],
    cmd_help={
    "help": "This is A TEST",
    "example": "{ch}helloworld"
    })
async def hello_world(client, message):
    mg = await edit_or_reply(message, "`Hello World! This Works!`")
```
### Custom Filters 📣

```python3
from main_startup.core.decorators import listen

@listen(filters.mentioned)
async def mentioned_(client, message):
    await message.reply_text("`Hello World! By The Way Why Did You Mention Me?`")
```

# X-Tra Plugins 🎸
* Please Visit [Xtra-Plugins](https://github.com/ramanveerji/Xtra-Plugins) To Checkout Xtra-Plugins.


# Licence 📋
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

* Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.

FridayUB is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

[![This Repo](https://telegra.ph//file/1e7411a9b611287d7bba9.jpg)](https://heroku.com/deploy?template=https://github.com/ramanveerji/FridayUserbot-Pyrogram)
