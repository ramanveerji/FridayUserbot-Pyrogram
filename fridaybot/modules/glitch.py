#    Copyright (C) Midhun KM 2020-2021
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

import os

from glitch_this import ImageGlitcher
from telethon.tl.types import MessageMediaPhoto
from pygifsicle import optimize
from fridaybot import CMD_HELP
import asyncio
import math
import os
import time
from fridaybot.function import progress, humanbytes, time_formatter
from fridaybot.function.FastTelethon import upload_file
from fridaybot.utils import friday_on_cmd, sudo_cmd
from fridaybot.function import convert_to_image

glitcher = ImageGlitcher()
DURATION = 200  # Set this to however many centiseconds each frame should be visible for
LOOP = 0  # Set this to how many times the gif should loop
# LOOP = 0 means infinite loop

sedpath = "./starkgangz/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)


@friday.on(friday_on_cmd(pattern=r"glitch"))
@friday.on(sudo_cmd(pattern=r"glitch", allow_sudo=True))
async def glitch(event):
    if event.fwd_from:
        return
    sed = await event.get_reply_message()
    okbruh = await event.edit("`Gli, Glitchiiingggg.....`")
    photolove = await convert_to_image(event, friday)
    pathsn = f"./starkgangz/@fridayot.gif"
    glitch_imgs = glitcher.glitch_image(photolove, 2, gif=True, color_offset=True)
    glitch_imgs[0].save(
        pathsn,
        format="GIF",
        append_images=glitch_imgs[1:],
        save_all=True,
        duration=DURATION,
        loop=LOOP,
    )
    c_time = time.time()
    optimize(pathsn)
    stark_m = await upload_file(
        	file_name="Glitched@FridayOt.gif",
            client=borg,
            file=open(pathsn, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading..", pathsn
                )
            ),
        )
    await borg.send_file(event.chat_id,
                         stark_m,
                         caption="Powered By @FridayOT")
    await okbruh.delete()
    for starky in (pathsn, photolove):
        if starky and os.path.exists(starky):
            os.remove(starky)


CMD_HELP.update(
    {
        "glitch": "**Glitch**\
\n\n**Syntax : **`.glitch <reply to a image>`\
\n**Usage :** Creates glitch gif of given image."
    }
)
