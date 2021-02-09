#    Copyright (C) @chsaiujwal 2020-2021
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

from fridaybot.utils import friday_on_cmd
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
from fridaybot.function import convert_to_image, is_nsfw
import requests
import string 
import random 


@friday.on(friday_on_cmd(pattern="(nsfw|checknsfw|nsfwdetect)$"))
@friday.on(sudo_cmd(pattern="nsfw$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "Reply To Any Image Idiot.")
        return
    reply_message = await event.get_reply_message()
    kok = await edit_or_reply(event, "`Processing...`")
    IdkWtf = await is_nsfw(reply_message)
    if IdkWtf is False:
      await kok.edit("Replied Image Is Not Nsfw.")
      return
    elif IdkWtf is True:
      await kok.edit("Replied Image is nsfw.")
      return 
    


CMD_HELP.update(
    {
        "nsfw_detector": "**Nsfw Detector**\
\n\n**Syntax : **`.nsfw <replying to the image>`\
\n**Usage :** Identifies If The Given Image Is Nsfw Or Not."
    }
)






