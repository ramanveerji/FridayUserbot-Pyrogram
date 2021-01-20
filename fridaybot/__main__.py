import logging
from pathlib import Path
from sys import argv
import pylast
import wget
from nospamplus.connect import Connect
from dotenv import load_dotenv
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from requests import get
from telegraph import Telegraph, exceptions, upload_file
from telethon import TelegramClient
from telethon.sessions import StringSession
from alchemysession import AlchemySessionContainer
import telethon.utils
from telethon import TelegramClient
from fridaybot.Configs import Config
from fridaybot.utils import load_module, start_assistant
from var import Var
Lastupdate = time.time()
sedprint = logging.getLogger("WARNING")
from var import Var
from fridaybot.modules.sql_helper import SESSION

container = AlchemySessionContainer(engine=SESSION)
session_name = Var.STRING_SESSION
session = container.new_session(session_name)

if Var.STRING_SESSION:
    bot = TelegramClient(StringSession(session), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)

sed = logging.getLogger("Friday")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
    else:
        bot.start()


import glob

path = "fridaybot/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "fridaybot/modules/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))
    sed.info("Friday And Assistant Bot Have Been Installed Successfully !")
else:
    sed.info("Friday Has Been Installed Sucessfully !")
    sed.info("You Can Visit @FridayOT For Any Support Or Doubts")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
