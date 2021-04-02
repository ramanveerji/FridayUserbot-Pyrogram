# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters

from database.welcomedb import add_welcome, del_welcome, welcome_info
from main_startup.config_var import Config
from main_startup.core.decorators import friday_on_cmd, listen
from main_startup.helper_func.basic_helpers import edit_or_reply


@friday_on_cmd(
    ["savewelcome"],
    cmd_help={
        "help": "Save Welcome Message!",
        "example": "{ch}savewelcome (reply to welcome message)",
    },
)
async def save_welcome(client, message):
    note_ = await edit_or_reply(message, "`Processing..`")
    if not message.reply_to_message:
        await note_.edit("Reply To Message To Save As Welcome Message!")
        return
    msg = message.reply_to_message
    cool = await msg.copy(Config.LOG_GRP)
    await add_welcome(message.chat.id, cool.message_id)
    await note_.edit(f"`Done! Welcome Message Saved!`")


@listen(filters.new_chat_members & filters.group)
async def welcomenibba(client, message):
    if not message:
        message.continue_propagation()
    if not message.chat:
        message.continue_propagation()
    if not await welcome_info(message.chat.id):
        message.continue_propagation()
    sed = await welcome_info(message.chat.id)
    await client.copy_message(
        from_chat_id=Config.LOG_GRP,
        chat_id=message.chat.id,
        message_id=sed["msg_id"],
        reply_to_message_id=message.message_id,
    )
    message.continue_propagation()


@friday_on_cmd(
    ["delwelcome"],
    cmd_help={"help": "Delete welcome Message!", "example": "{ch}delwelcome"},
)
async def del_welcomez(client, message):
    note_ = await edit_or_reply(message, "`Processing..`")
    if not await welcome_info(message.chat.id):
        await note_.edit("`Welcome Message Not Found In This Chat!`")
        return
    await del_welcome(message.chat.id)
    await note_.edit(f"`Welcome Message Deleted Successfully!`")


@friday_on_cmd(
    ["welcome"],
    cmd_help={"help": "Current Welcome Message!", "example": "{ch}welcome"},
)
async def show_welcome(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    sed = await welcome_info(message.chat.id)
    if sed is False:
        await pablo.edit("`No Welcome Found In This Chat...`")
        return
    mag = f""" Welcome Message In Correct Chat Is :"""
    await client.copy_message(
        from_chat_id=Config.LOG_GRP,
        chat_id=message.chat.id,
        message_id=sed["msg_id"],
        reply_to_message_id=message.message_id,
    )
    await pablo.edit(mag)
