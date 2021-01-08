"""
Syntax : .gps <location name>
credits :@mrconfused
"""

# help from @sunda005 and @SpEcHIDe
# don't edit credits

from geopy.geocoders import Nominatim
from telethon.tl import types
import requests
import urllib.parse
from fridaybot import CMD_HELP
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd(pattern="gps ?(.*)"))
@friday.on(sudo_cmd(pattern="gps ?(.*)", allow_sudo=True))
async def gps(event):
    starkislub = await edit_or_reply(event, "Processing")
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    address = event.pattern_match.group(1)

    if not address:
        return await starkislub.edit("what should i find give me location.")

    await starkislub.edit("finding")

    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    try:
        lat = response[0]["lat"]
	lon = response[0]["lon"]
        await reply_to_id.reply(
            input_str, file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon))
        )
        await event.delete()
    except:
        await starkislub.edit("location not found. please try giving input with country.")


CMD_HELP.update(
    {
        "gps": "**Gps**\
\n\n**Syntax : **`.gps <location>`\
\n**Usage :** this plugin gives gps to the location."
    }
)
