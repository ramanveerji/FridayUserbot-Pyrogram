# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.


from main_startup.core.decorators import friday_on_cmd
from main_startup.core.startup_helpers import run_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text
from main_startup.__main__ import bot


@friday_on_cmd(
    ["help", "helper"],
    cmd_help={
        "help": "Gets Help Menu",
        "example": "{ch}help",
    },
)
async def help(client, message):
    starkbot = await bot.get_me()
    bot_username = starkbot.username
    nice = await client.get_inline_bot_results(bot=bot_username, query="help")
    await client.send_inline_bot_result(message.chat.id, nice.query_id, nice.results[0].id, hide_via=True)
    await message.delete()
