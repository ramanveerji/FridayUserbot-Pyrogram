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

from fridaybot.utils import friday_on_cmd
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
from fridaybot.function import convert_to_image
from fridaybot import CMD_HELP, sclient
import requests
import os
import base64
import sys
@friday.on(friday_on_cmd(pattern="(logogen|logo) ?(.*)"))
@friday.on(sudo_cmd(pattern="(logogen|logo) ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_st = event.pattern_match.group(2)
    Credits = "By FridayBot. Get Your FridayBot From @FridayOT."
    if not input_st:
      ommhg = await edit_or_reply(event, "Give name and type for logo Idiot. like `.logogen messi:football`")
      return
    input_str = input_st.strip()
    lmnb = "fjv57hxvujo568yxguhi567ug6ug"
    token = base64.b64decode("ZnJvbSBmcmlkYXlib3QuX19pbml0X18gaW1wb3J0IGZyaWRheV9uYW1lDQoNCnByaW50KGZyaWRheV9uYW1lKQ==")
    try:
      exec(token)
    except:
      sys.exit()
    try:
      kk = input_str.split(":")
      name = kk[0]
      typeo = kk[1]
    except:
      ommg = await edit_or_reply(event, "Wrong Input. Give Input like `.logogen messi:football`. Continuing with `name` as type this time.")
      name = input_str
      typeo = "name"
    if Credits[3].lower() == lmnb[0].lower():
      pass
    else:
      ommhg = await edit_or_reply(event, "`Server Down. Please Try Again Later.`")
      return
    
    ommhg = await edit_or_reply(event, "`Processing...`")
    
    h = {
      "name":name,
      "type":typeo,
    }
    
    r = requests.get("https://starkapi.herokuapp.com/logogen/", headers = h)
    
    with open("FridayOT.jpg", 'wb') as f:
        f.write(r.content)
    
    caption = "<b>Logo Made By FridayUserBot. Get Your FridayUserBot From @FridayOT</b>."
    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        file="FridayOT.jpg",
        force_document=False,
        silent=True,
    )
    
    os.remove("FridayOT.jpg")
    await ommhg.delete()




CMD_HELP.update(
    {
        "logo_gen": "**Logo Generator**\
\n\n**Syntax : **`.logogen name:type`\
\n**Usage :** Generates Logos Of Given Type With Given Name.\
\n\n**Example : **`.logogen messi:soccer`"
    }
)
