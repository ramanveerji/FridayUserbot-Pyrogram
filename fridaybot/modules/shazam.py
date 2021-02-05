from fridaybot.function import fetch_audio
import requests
from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
import os
import random
import string
from pathlib import Path

@friday.on(friday_on_cmd(pattern="shazam"))
@friday.on(sudo_cmd(pattern="shazam", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        ommhg = await edit_or_reply(event, "Reply To The Audio.")
        return
    if Path("friday.mp3").is_file():
      os.remove("friday.mp3")
    
    ommhg = await edit_or_reply(event, "Downloading The Song. 🙂😄")
    kkk = await fetch_audio(event, borg)
    credit = "By Friday. Get Your Friday From @FridayOt"
    downloaded_file_name = str("friday.mp3")
    
    f = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    
    
    await ommhg.edit("searching for the song 🔍🧐")
    r = requests.post("https://starkapi.herokuapp.com/shazam/", files = f)
    try:
      xo = r.json()
    except:
      return
    try:
      xo = r.json()
      xoo = xo.get("response")
      zz = xoo[1]
      zzz = zz.get("track")
      Col = zzz.get("sections")[3]
      nt = zzz.get("images")	
      image = nt.get("coverarthq")
      by = zzz.get("subtitle")
      title = zzz.get("title")
      message = f"""<b>Song Identified</b>
<b>Song Name : </b>{title}
<b>Song By : </b>{by}

<u><b>Identified By Friday.
Get Your Friday From</b></u> @fridayot.
"""
      await borg.send_message(
        event.chat_id,
        message,
        parse_mode="HTML",
        file=image,
        force_document=False,
        silent=True,
      )
      os.remove(downloaded_file_name)
      await ommhg.delete()
    except:
      if xo.get("success") ==False:
        errer = xo.get("success")
        ommhg = await edit_or_reply(event, errer)
        os.remove(downloaded_file_name)
        return
      ommhg = await edit_or_reply(event, "Song Not Found. Please Try Again.")
      os.remove(downloaded_file_name)
      return

CMD_HELP.update(
    {
        "shazam": "**Shazam**\
\n\n**Syntax : **`.shazam <replying to the song>`\
\n**Usage :** Identifies The Song."
    }
)

