import asyncio
import os
import time
import time as t
import zipfile
from datetime import datetime
from fridaybot import CMD_HELP
from fridaybot.function import convert_to_image, crop_vid, runcmd
from fridaybot.utils import friday_on_cmd, sudo_cmd
from pdf2docx import parse
import glob
import string 
import random 
import uuid



if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
  os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
  

@friday.on(friday_on_cmd(pattern="p2dcl(?: |$)(.*)"))
async def starky(event):
    un = event.pattern_match.group(1)
    rndm = uuid.uuid4().hex
    frid = uuid.uuid4().hex
    diro = f"./{rndm}/"
    dirb = f"./{frid}/"
    os.makedirs(diro)
    os.makedirs(dirb)
    media_count = 0
    text_count = 0
    if un:
        chnnl = un
    else:
        chnnl = event.chat_id
    
    await event.edit(f"**Fetching All Files From This Channel**")
    try:
        chnnl_msgs = await borg.get_messages(chnnl, limit=3000)
    except:
        await event.edit("**Unable To fetch Messages !** \n`Please, Check Channel Details And IF THere Are Any Media :/`")
        return
    
    
    total = int(chnnl_msgs.total)
    
    await event.edit(f"**Downloading {total} Media/Messages**")
    for d in chnnl_msgs:
        if d.media:
            media_count += 1
            await borg.download_media(d.media, diro)
        if d.text:
            text_count += 1
            
    await event.edit(f"**Total Media :** `{total}` \n**Downloaded Media :** `{media_count}` \n**Total Texts :** `{text_count}` \n**Now Converting Files.**")
    
    
    Azx = glob.glob(f"{diro}*.pdf")
    
    for friday in Azx:
      N = 9
      
      res =''.join(random.choices(string.ascii_uppercase+string.digits, k = N))
      pdf_file = friday
      docx_file = f'{dirb}{str(res)}.docx'
      
      parse(pdf_file, docx_file, start=0, end=None)
      
      
    Ax = glob.glob(f"{dirb}*.docx")
    for pop in Ax:
      await borg.send_file(event.chat_id, pop, caption=f"**Total Media :** `{total}` \n**Downloaded Media :** `{media_count}` \n**Total Texts  :** `{text_count}` \n**By @fridayot**")
    Azx = glob.glob(f"{diro}*")
    Azpx = glob.glob(f"{dirb}*")
    for x in Azx:
      os.remove(x)
    
    for pop in Azpx:
      os.remove(pop)
    
    
    os.rmdir(diro)
    os.rmdir(dirb)


  
@friday.on(friday_on_cmd(pattern=r"pdf2docx"))
@friday.on(sudo_cmd(pattern=r"pdf2docx", allow_sudo=True))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Pdf File.")
        return
    hmmu = await event.reply("hmm... Please Wait...🚶")
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)
    
    hmmu = await event.reply("hmm... Please Wait...🚶")
    
    pdf_file = starky
    docx_file = './fridaybot/DOWNLOADS/FRIDAYOT.docx'
    
    parse(pdf_file, docx_file, start=0, end=None)
    
    await borg.send_file(
        event.chat_id, docx_file, caption=f"*PDF Converted Into Docx by Friday bot. Get your Friday From @FRIDAYOT."
    )
    os.remove(pdf_file)
    os.remove(docx_file)
    await event.delete()




CMD_HELP.update(
    {
        "fileTools": "**File Tools**\
\n\n**Syntax : **`.pdf2docx <reply to pdf>`\
\n**Usage :** Converts Given Pdf Into Docx.\
\n\n**Syntax : **`.p2dcl <channel username>`\
\n**Usage :** Converts All The Pdf's From Channel Into Docx."
    }
)
