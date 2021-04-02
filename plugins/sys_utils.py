# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

import platform
import re
import socket
import time
import uuid
from datetime import datetime
import sys
import psutil
from pyrogram import __version__
from os import environ, execle, path, remove
from main_startup import friday_version, start_time, Config
from main_startup.core.decorators import friday_on_cmd
from main_startup.helper_func.basic_helpers import (
    edit_or_reply,
    get_readable_time,
    humanbytes,
)


@friday_on_cmd(
    ["ping", "pong"],
    cmd_help={"help": "Check Bot Uptime!", "example": "{ch}ping"},
)
async def pingy(client, message):
    start = datetime.now()
    hmm = await edit_or_reply(message, "`Pong!`")
    uptime = get_readable_time((time.time() - start_time))
    myself = await client.get_me()
    if not myself.username:
        mys = myself.id
    else:
        mys = f"@{myself.username}"
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await hmm.edit(
        f"**█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄**\n➲ `{round(ms)}ms` \n➲ `{uptime}` \n➲ `{mys}`"
    )


@friday_on_cmd(
    ["alive"],
    cmd_help={"help": "Get Alive Message Of Your Bot.!", "example": "{ch}alive"},
)
async def amialive(client, message):
    img_ = Config.ALIVE_IMG
    me_ = client.me.first_name
    alive = f"""
**{me_}'s Friday-UserBot is Alive!**
➠ **OS :** __{platform.system()}__
➠ **CPU :** __{len(psutil.Process().cpu_affinity())}__
➠ **Version :** __{friday_version}__
➠ **Uptime :** __{get_readable_time((time.time() - start_time))}__
➠ **PyroGram Version :** __{__version__}__
➠ **Python Version :** __{platform.python_version()}__
➠ **(C) @DEVSEXPO 2020-2021**
"""
    if message.reply_to_message:
        await client.send_photo(message.chat.id, img_, caption=alive, reply_to_message_id=message.reply_to_message.message_id)
    else:
        await client.send_photo(message.chat.id, img_, caption=alive)


@friday_on_cmd(
    ["sysinfo", "neofetch"],
    cmd_help={"help": "Get System Information!", "example": "{ch}sysinfo"},
)
async def give_sysinfo(client, message):
    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    ram = humanbytes(round(psutil.virtual_memory().total))
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    du = psutil.disk_usage(client.workdir)
    psutil.disk_io_counters()
    disk = f"{humanbytes(du.used)} / {humanbytes(du.total)} " f"({du.percent}%)"
    cpu_len = len(psutil.Process().cpu_affinity())
    neat_msg = f"""**System Info**
    
**PlatForm :** `{splatform}`
**PlatForm - Release :** `{platform_release}`
**PlatFork - Version :** `{platform_version}`
**Architecture :** `{architecture}`
**Hostname :** `{hostname}`
**IP :** `{ip_address}`
**Mac :** `{mac_address}`
**Processor :** `{processor}`
**Ram : ** `{ram}`
**CPU :** `{cpu_len}`
**CPU FREQ :** `{cpu_freq}`
**DISK :** `{disk}`
    """
    await edit_or_reply(message, neat_msg)

@friday_on_cmd(
    ["restart"],
    cmd_help={"help": "Restart Your Bot!", "example": "{ch}restart"},
)
async def wow_restart(client, message):
    await edit_or_reply(message, "`🔁 Restarting... 🔁`")
    args = [sys.executable, "-m", "main_startup"]
    execle(sys.executable, *args, environ)
    return
