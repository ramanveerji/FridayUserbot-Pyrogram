from fridaybot.utils import friday_on_cmd
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
from fridaybot.function import convert_to_image
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
    Credits = "By Friday. Get Your Friday From @Friday_OT"
    Reply_message = Credits
    if not reply_message.media:
      await edit_or_reply(event, "Reply To Any Image. Not To text or anything else.")
      return
    tokez = Reply_message[3:9].lower()
    loZ = Reply_message[3].lower()
    nsfew = "nsfw[001][5556]^√~~×{{}∆}÷]][™™®®®--44447££6"
    kok = await edit_or_reply(event, "Processing.")
    nsf=  nsfew[2]
    if loZ == nsf:
      N = 15
    else:
      N = 14
    img = await convert_to_image(event, borg)
    res = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N))
    token = str(res)
    f = {"file": (img, open(img, "rb"))}
    h = {
      "by":tokez,
      "token":token
    }
    r = requests.post("https://starkapi.herokuapp.com/nsfw/", files = f, headers = h).json()
    if r.get("success") is False:
      await kok.edit(r.get("error"))
      return
    elif r.get("is_nsfw") is True:
      await kok.edit("Replied Image is nsfw.")
    elif r.get("is_nsfw") is False:
      await kok.edit("Replied Image is Not nsfw.")


CMD_HELP.update(
    {
        "nsfw_detector": "**Nsfw Detector**\
\n\n**Syntax : **`.nsfw <replying to the image>`\
\n**Usage :** Identifies If The Given Image Is Nsfw Or Not."
    }
)






