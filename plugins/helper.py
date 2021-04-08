# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.


from main_startup import CMD_LIST, bot
from main_startup.core.decorators import Config, friday_on_cmd
from main_startup.core.startup_helpers import run_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text


@friday_on_cmd(
    ["help", "helper"],
    cmd_help={
        "help": "Gets Help Menu",
        "example": "{ch}help",
    },
)
async def help(client, message):
    help_t = "<b>Command Names :</b> \n\n"
    if bot:
        starkbot = await bot.get_me()
        bot_username = starkbot.username
        nice = await client.get_inline_bot_results(bot=bot_username, query="help")
        await client.send_inline_bot_result(
            message.chat.id, nice.query_id, nice.results[0].id, hide_via=True
        )
        await message.delete()
    else:
        f_ = await edit_or_reply(message, "`Please Wait!`")
        cmd_ = get_text(message)
        if not cmd_:
            for i in CMD_LIST:
                if i:
                    help_t += f"▶ {i} \n"
            help_t += f"If You Wanna Check Command Info And List About A Specfic Plugin, Use <code>{Config.COMMAND_HANDLER}help (file_name)</code>"
            await f_.edit(help_t)
        else:
            if cmd_ not in CMD_LIST.keys():
                await f_.edit("`404: Plugin Not Found!`")
                return
            await f_.edit(CMD_LIST[cmd_])


@friday_on_cmd(
    ["ahelp", "ahelper"],
    cmd_help={
        "help": "Gets Help List & Info",
        "example": "{ch}ahelp (cmd_name)",
    },
)
async def help_(client, message):
    help_t = "<b>Command Names :</b> \n\n"
    f_ = await edit_or_reply(message, "`Please Wait!`")
    cmd_ = get_text(message)
    if not cmd_:
        for i in CMD_LIST:
            if i:
                help_t += f"➲ {i} \n"
        help_t += f"\nIf You Wanna Check Command Info And List About A Specfic Plugin, Use <code>{Config.COMMAND_HANDLER}help (file_name)</code>"
        await f_.edit(help_t)
    else:
        if cmd_ not in CMD_LIST.keys():
            await f_.edit("`404: Plugin Not Found!`")
            return
        await f_.edit(CMD_LIST[cmd_])
