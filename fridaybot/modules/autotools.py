#    Copyright (C) @DevsExpo 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
    sed = await edit_or_reply(event, "`Started AutoName Your Name Will Be Changed Every 1 Min, According To TimeZone Given. To Terminate This Process Use .stop Cmd`")
    scheduler.add_job(auto_name, 'interval', args=[event.pattern_match.group(1)], minutes=1, id='autoname')

@friday.on(friday_on_cmd(pattern="autobio(?: |$)(.*)"))
@friday.on(sudo_cmd(pattern="autobio(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    sed = await edit_or_reply(event, "`Started AutoBio Your Bio Will Be Changed Every 1 Min, According To TimeZone Given. To Terminate This Process Use .stop Cmd`")
    scheduler.add_job(auto_bio, 'interval', args=[event.pattern_match.group(1)], minutes=1, id='autobio')

@friday.on(friday_on_cmd(pattern="stop$"))
@friday.on(sudo_cmd(pattern="stop$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    sed = await edit_or_reply(event, "`Checking Recived Input :/`")
    try:
        scheduler.shutdown()
    except:
        await event.edit("`Are You Fking Insane?`")
        return
    await sed.edit("`All Auto Tools Has Been Terminated`")
    
scheduler.start()

CMD_HELP.update(
    {
        "autoname": "**Autoname**\
\n\n**Syntax : **`.autoname`\
\n**Usage :** Change your Name With Time"
    }
)
