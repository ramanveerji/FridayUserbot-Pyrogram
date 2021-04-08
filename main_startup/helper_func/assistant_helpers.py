# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from functools import wraps

from main_startup.helper_func.basic_helpers import get_all_pros, is_admin_or_owner


def _check_admin(func):
    @wraps(func)
    async def magic_admin(client, message):
        is_a_o = await is_admin_or_owner(message, message.from_user.id)
        if is_a_o:
            await func(client, message)
        else:
            await message.reply_text("`>> You Should Be Admin / Owner To Do This! >>`")

    return magic_admin


def _check_owner_or_sudos(func):
    @wraps(func)
    async def magic_owner(client, message):
        use_ = await get_all_pros()
        if message.from_user.id in use_:
            await func(client, message)
        else:
            await message.reply_text("`>> You Should Be Owner / Sudo To Do This! >>`")

    return magic_owner
