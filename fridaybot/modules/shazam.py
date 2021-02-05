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
    
    credit = "By Friday. Get Your Friday From @FridayOT"
    
    if Path("friday.mp3").is_file():
      os.remove("friday.mp3")
    
    ommhg = await edit_or_reply(event, "Downloading The Song. 🙂😄")
    pl = credit[3].lower()
    kkk = await fetch_audio(event, borg)
    credit = "By Friday. Get Your Friday From @FridayOt"
    downloaded_file_name = str("friday.mp3")
    k6 = "flowrence formula"
    f = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    m0 = k6[0]
    
    await ommhg.edit("searching for the song 🔍🧐")
    if pl == m0:
       No = "15"
      
    else:
      No = "14"
    N = int(No)
    res = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N)) 
    oate = str(res)
    h = {
      "token" : oate
    }
    r = requests.post("https://starkapi.herokuapp.com/shazam/", files = f, headers = h)
    try:
      xo = r.json()
      xoo = xo.get("response")
      zz = xoo[1]
    except:
      xo = r.json()
      if xo.get("success") ==False:
        errer = xo.get("success")
        await ommhg.edit(errer)
        os.remove(downloaded_file_name)
        return
      await ommhg.edit("Song Not Found. Please Try Again.")
      os.remove(downloaded_file_name)
      return
    try:
      xo = r.json()
      zz = xo.get("response")
      #zz = xoo[1]
      zzz = zz.get("track")
      nt = zzz.get("images")
      image = nt.get("coverarthq")
      Col = zzz.get("sections")[3]
      
      by = zzz.get("subtitle")
      title = zzz.get("title")
      message = f"""<b>Song Identified</b>
<b>Song Name : </b>{title}
<b>Song By : </b>{by}

<u><b>Identified By Friday.
Get Your Friday From</b></u> @FridayOT.
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
\n**Usage :** Identifies The Song.\
\n\n**Note : **The Person In Picture Really Doesn't Exist."
    }
)

