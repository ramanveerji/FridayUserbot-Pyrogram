# All 3 Clients

from telethon import TelegramClient
from telethon.sessions import StringSession
from fridaybot.Configs import Config

if Config.STRING_SESSION:
    session_name = str(Config.STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), Config.APP_ID, Config.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Config.APP_ID, Config.API_HASH)
if Config.STRING_SESSION_2:
    client2 =  TelegramClient(StringSession(Config.STRING_SESSION_2), Config.APP_ID, Config.API_HASH)
else:
    client2 = None
if Config.STRING_SESSION_3:
    client3 =  TelegramClient(StringSession(Config.STRING_SESSION_3), Config.APP_ID, Config.API_HASH)
else:
    client3 = None
