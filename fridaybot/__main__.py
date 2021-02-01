import logging
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from fridaybot import bot, client2, client3
from fridaybot.Configs import Config
from telethon.tl.types import InputMessagesFilterDocument
from fridaybot.utils import load_module, start_assistant, load_module_dclient
from fridaybot.Configs import Config

sed = logging.getLogger("Friday")

        
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)
    
async def lol_s(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)
    
def multiple_client():
    if client2:
        sed.info("Starting Client 2")
        try:
            sedbruh = None
            client2.start()
            client2.loop.run_until_complete(lol_s(client2))
        except:
            sedbruh = True
            sed.info("Client 2 Failed To Load. Check Your String.")
    if client3:
        sed.info("Starting Client 3")
        try:
            lmaobruh = None
            cleint3.start
            client3.loop.run_until_complete(lol_s(client3))
        except:
            lmaobruh = True
            sed.info("Client 3 Failed To Load.")
    if not client2:
        sedbruh = True
    if not client3:
        lmaobruh = True
    return sedbruh, lmaobruh    

async def get_other_plugins(Config, client_s, sed):
    try:
        a_plugins = await client_s.get_messages(
            entity=Config.LOAD_OTHER_PLUGINS_CHNNL,
            filter=InputMessagesFilterDocument,
            limit=None,
            search=".py",
        )
    except:
        sed.info("Failed To Other Modules :(")
        return
    sed.info(f"Downloading. {int(a_plugins.total)} Plugins !")
    for keky in a_plugins:
        await client_s.download_media(keky.media, "fridaybot/modules/")
    sed.info("Extra Plugins Downloaded.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Config.TG_BOT_TOKEN_BF_HER is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
        ).start(bot_token=Config.TG_BOT_TOKEN_BF_HER)
        failed2, failed3 = multiple_client()
        bot.loop.run_until_complete(add_bot("MyAssistantBot"))
    else:
        bot.start()
        failed2, failed3 = multiple_client()

if Config.LOAD_OTHER_PLUGINS:
        bot.loop.run_until_complete(get_other_plugins(Config, bot, sed))
        
import glob

path = "fridaybot/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            load_module(shortname.replace(".py", ""))    
        except Exception as e:
            sed.info("------------------------")
            sed.info("Failed To Load : " + str(shortname.replace(".py", "")) + f" Error : {str(e)}")
            sed.info("------------------------")
        if failed2 is None:
            try:
                load_module_dclient(shortname.replace(".py", ""), client2)
            except:
                pass
        if failed3 is None:
            try:
                load_module_dclient(shortname.replace(".py", ""), client3)
            except:
                pass

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
