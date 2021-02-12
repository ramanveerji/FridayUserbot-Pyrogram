import asyncio
import time
import random
from telethon.tl import functions
from fridaybot.Configs import Config
from fridaybot import bot
import pytz
import asyncio
import os
from datetime import datetime
m = logging.getLogger("AUTOTOOLS")

bio_temp = ["Making History.", "I'm on energy-saving mode.", "Success is in my blood.", "Life F$@ks me, now it's my turn.", "Error 400: Bio unavailable."]

async def auto_name(name=None):
    TZ = pytz.timezone(Config.TZ)
    datetime_tz = datetime.now(TZ)
    nameof = name if name else Config.ALIVE_NAME
    oof = datetime_tz.strftime(f"🕒 %Y/%m/%d ⚡{nameof}⚡ 📅%H:%M:%S")
    try:
        await bot(
                functions.account.UpdateProfileRequest(
                    first_name=oof
                )
            )
    except Exception as e:
        m.warning(f"Failed AutoName Due To : {e}")
    return    
    
async def auto_bio(bio=None):
    TZ = pytz.timezone(Config.TZ)
    datetime_tz = datetime.now(TZ)
    bioof = name if name else random.choice(bio_temp)
    oof = datetime_tz.strftime(f"🕒 %Y/%m/%d {bioof} 📅%H:%M:%S")
    try:
        await bot(
                functions.account.UpdateProfileRequest(
                    about=oof
                )
            )
    except Exception as e:
        m.warning(f"Failed AutoBio Due To : {e}")
    return    
