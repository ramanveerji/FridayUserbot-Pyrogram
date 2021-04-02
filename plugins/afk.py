# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from main_startup.config_var import Config
from main_startup.core.decorators import friday_on_cmd, listen
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text
from datetime import datetime
import asyncio
from main_startup.helper_func.logger_s import LogIt

from database.afk import (
    no_afk,
    go_afk,
    check_afk
)



@friday_on_cmd(
    ["afk"],
    cmd_help={
        "help": "Set AFK!",
        "example": "{ch}afk",
    },
)
async def set_afk(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    msge = None
    msge = get_text(message)
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    log = LogIt(message)
    if msge:
        msg = f"**My Master Seems To Be Too Busy 👀.** \n__He Going Afk Because Of__ `{msge}`"
        await log.log_msg(client, f"#AfkLogger Afk Is Active And Reason is {msge}",)
        await go_afk(afk_start, msge)
    else:
        msg = f"**I Am Busy And I Am Going Afk**."
        await log.log_msg(client, f"#AfkLogger Afk Is Active",)
        await go_afk(afk_start) 
    await pablo.edit(msg)
        
@listen(filters.mentioned & ~filters.me & ~filters.bot & ~filters.edited & filters.incoming)
async def afk_er(client, message):
    lol = await check_afk()
    if not lol:
        message.continue_propagation()
    reason = lol["reason"]
    if reason == "":
        reason = None
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    afk_since = "**a while ago**"
    message_to_reply = (f"I Am **[AFK]** Right Now. \n**Last Seen :** `{total_afk_time}`\n**Reason** : `{reason}`" if reason else f"I Am **[AFK]** Right Now. \n**Last Seen :** `{total_afk_time}`")
    LL = await message.reply(message_to_reply)
    await asyncio.sleep(8)
    await LL.delete()
    message.continue_propagation()
        
@listen(filters.outgoing & filters.me)
async def no_afke(client, message):
    lol = await check_afk()
    if not lol:
        message.continue_propagation()
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    kk = await message.reply(f"""__Pro is Back Alive__\n**No Longer afk.**\n `I Was afk for:``{total_afk_time}`""",)
    await kk.delete()
    await no_afk()
    log = LogIt(message)
    await log.log_msg(client, f"#AfkLogger User is Back Alive ! No Longer Afk\n AFK for : {total_afk_time} ")
    message.continue_propagation()
