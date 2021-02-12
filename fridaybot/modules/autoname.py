"""Auto Profile Updation Commands
.autoname"""
import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions
from uniborg.util import edit_or_reply, friday_on_cmd, sudo_cmd
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.executors.asyncio import AsyncIOExecutor
from fridaybot.function.auto_tools import auto_name
from fridaybot import ALIVE_NAME, CMD_HELP


@friday.on(friday_on_cmd(pattern="autoname"))  # pylint:disable=E0602
@friday.on(sudo_cmd(pattern="autoname", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    sed = await edit_or_reply(event, "`Started AutoName.`")
    scheduler = AsyncIOScheduler(
        executors={
    'default': AsyncIOExecutor(),
        }
    )
    scheduler.add_job(auto_name, 'interval', args=[event.pattern_match.group(1)], minutes=5)
    scheduler.start()

    


CMD_HELP.update(
    {
        "autoname": "**Autoname**\
\n\n**Syntax : **`.autoname`\
\n**Usage :** Change your Name With Time"
    }
)
