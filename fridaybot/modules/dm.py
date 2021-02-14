# Concept got from Telebot
# By @HeisenbergTheDanger and @xditya

from telethon import *

from fridaybot import CMD_HELP

from fridaybot.utils import friday_on_cmd
from telethon.tl.functions.users import GetFullUserRequest


from fridaybot.utils import register



@friday.on(friday_on_cmd(pattern="dm ?(.*)"))

async def _(event):
    if event.fwd_from:
        return
    d = event.pattern_match.group(1)

    c = d.split(" ")  

    chat_id = c[1]
    try:  
        chat_id = int(chat_id)
    
    except BaseException:  
        H = await event.client(GetFullUserRequest(chat_id))
        chat_id = H.user.id
    msg = ""
    masg = await event.get_reply_message() 
    if event.reply_to_msg_id:
        await borg.send_message(chat_id, masg)
        await event.edit("Message Delivered Succesufully ")
    for i in c[1:]:
        msg += i + " " 
    if msg == "":  
        return
    try:
        await borg.send_message(chat_id, msg)
        await event.edit("Message Delivered")
    except BaseException:  
        await event.edit(".dm (username) (text)")


CMD_HELP.update(
    {
        "dm": ".dm (username) (text)\n or\n .dm (username)(reply to msg)\n forward the replyed msg without the forward tag"
    }
)
