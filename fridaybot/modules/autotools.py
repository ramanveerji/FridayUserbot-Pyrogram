import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions
from uniborg.util import edit_or_reply, friday_on_cmd, sudo_cmd
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.executors.asyncio import AsyncIOExecutor
from fridaybot.function.auto_tools import auto_name, auto_bio
from fridaybot import ALIVE_NAME, CMD_HELP

scheduler = AsyncIOScheduler(executors={'default': AsyncIOExecutor()})

@friday.on(friday_on_cmd(pattern="autoname(?: |$)(.*)"))
@friday.on(sudo_cmd(pattern="autoname(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    sed = await edit_or_reply(event, "`Started AutoName Your Name Will Be Changed Every 1 Min, According To TimeZone Given. To Terminate This Process Do A Restart`")
    scheduler.add_job(auto_name, 'interval', args=[event.pattern_match.group(1)], minutes=1, id='autoname')
    scheduler.start()

@friday.on(friday_on_cmd(pattern="autobio(?: |$)(.*)"))
@friday.on(sudo_cmd(pattern="autobio(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    sed = await edit_or_reply(event, "`Started AutoBio Your Bio Will Be Changed Every 1 Min, According To TimeZone Given. To Terminate This Process Do A Restart`")
    scheduler.add_job(auto_bio, 'interval', args=[event.pattern_match.group(1)], minutes=1, id='autobio')
    scheduler.start()

@friday.on(friday_on_cmd(pattern="stop$"))
@friday.on(sudo_cmd(pattern="stop$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    sed = await edit_or_reply(event, "`Checking Recived Input :/`")
    try:
        scheduler.shutdown()
    except:
        await event.edit("Are You Fking Insane?")
        return
    await event.edit(f"`Process Terminated.`")  
    


CMD_HELP.update(
    {
        "autoname": "**Autoname**\
\n\n**Syntax : **`.autoname`\
\n**Usage :** Change your Name With Time"
    }
)
