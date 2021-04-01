# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from main_startup.core.decorators import friday_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply
from main_startup.helper_func.plugin_helpers import is_nsfw


@friday_on_cmd(
    ["nsfw"],
    cmd_help={
        "help": "Check Replied Message Is Nsfw Or Not!",
        "example": "{ch}nsfw (reply to image/video)",
    },
)
async def nsfw(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    if not message.reply_to_message:
        await pablo.edit("reply to a image...!")
        return
    gs = await is_nsfw(client, message)
    if gs is True:
        await pablo.edit("Replied Image Is Nsfw")
    if gs is False:
        await pablo.edit("Replied Image Is Not Nsfw")
