# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import ChatPermissions

from database.nsfw_watch_db import add_chat, get_all_nsfw_chats, is_chat_in_db, rm_chat
from main_startup.core.decorators import friday_on_cmd, listen
from main_startup.helper_func.basic_helpers import edit_or_reply, is_admin_or_owner
from main_startup.helper_func.logger_s import LogIt
from main_startup.helper_func.plugin_helpers import is_nsfw


@friday_on_cmd(
    ["anw", "add_nsfw"],
    group_only=True,
    cmd_help={"help": "Add Chat To Nsfw Watch!", "example": "{ch}add_nsfw"},
)
async def add_nsfw(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    if await is_chat_in_db(message.chat.id):
        await pablo.edit("`This Chat is Already In My DB`")
        return
    me = await client.get_me()
    lol = await is_admin_or_owner(message, me.id)
    if not lol:
        await pablo.edit("`I Am Not An Admin!`")
        return
    await add_chat(message.chat.id)
    await pablo.edit("Successfully Added Chat To NSFW Watch.")


@friday_on_cmd(
    ["rmnw", "remove_nsfw"],
    group_only=True,
    cmd_help={"help": "Remove Chat From Nsfw Watch!", "example": "{ch}remove_nsfw"},
)
async def remove_nsfw(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    if not await is_chat_in_db(message.chat.id):
        await pablo.edit("`This Chat is Not in dB.`")
        return
    await rm_chat(message.chat.id)
    await pablo.edit("`Successfully Removed Chat From NSFW Watch.`")


@listen(filters.incoming & filters.media & ~filters.private & ~filters.channel)
async def nsfw_watch(client, message):
    lol = await get_all_nsfw_chats()
    if len(lol) == 0:
        message.continue_propagation()
    if not await is_chat_in_db(message.chat.id):
        message.continue_propagation()
    hot = await is_nsfw(client, message, False)
    if not hot:
        message.continue_propagation()
    else:
        try:
            await message.delete()
            await client.restrict_chat_member(
                message.chat.id,
                message.from_user.id,
                ChatPermissions(can_send_messages=False),
            )
        except:
            pass
        lolchat = await client.get_chat(message.chat.id)
        ctitle = lolchat.title
        if lolchat.username:
            hehe = lolchat.username
        else:
            hehe = message.chat.id
        midhun = await client.get_users(message.from_user.id)
        await message.delete()
        if midhun.username:
            Escobar = midhun.username
        else:
            Escobar = midhun.id
        log = LogIt(message)
        await log.log_msg(
            client,
            f"**#NSFW_WATCH** \n**Chat :** `{hehe}` \n**Nsfw Sender - User / Bot :** `{Escobar}` \n**Chat Title:** `{ctitle}`",
        )
        message.continue_propagation()
