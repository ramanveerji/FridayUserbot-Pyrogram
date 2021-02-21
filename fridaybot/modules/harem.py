# Made By @Midhun_xD, Base Of Module By @kandnub
# Copyright (C) 2019 The Raphielscape Company LLC.
# Thanks to @kandnub, for Base.
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

import io
import os
import re
import urllib
import shutil
from re import findall
import requests
from bs4 import BeautifulSoup
from telethon import events
from PIL import Image
from fridaybot.function import convert_to_image
from fridaybot import CMD_HELP


opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]

from fridaybot.utils import errors_handler, register, friday_on_cmd

async def ParseSauce(googleurl):
    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")
    results = {"similar_images": "", "best_guess": ""}
    try:
        for similar_image in soup.findAll("input", {"class": "gLFyf"}):
            url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
                similar_image.get("value")
            )
            results["similar_images"] = url
    except BaseException:
        pass
    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()
    return results

if Config.ENABLE_HAREM:
    @friday.on(events.NewMessage(func=lambda x: x.sender_id == int(792028928)))
    async def ihave3000waifu_uwantsome(event):
        if event.media:
            if 'Add' in event.raw_text:
                logger.info("OwO")
                waifu_moment = await friday.download_media(event.media)
                searchUrl = "https://www.google.com/searchbyimage/upload"
                file_img = {"encoded_image": (waifu_moment, open(waifu_moment, "rb")), "image_content": ""}
                response = requests.post(searchUrl, files=file_img, allow_redirects=False)
                if response != 400:
                    await borg.send_message(Config.PRIVATE_GROUP_ID, "`A Waifu Appeared By Was Unable To Parse Image! Sorry :(`")
                    return
                fetchUrl = response.headers["Location"]
                match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
                guess = match["best_guess"]
                if not guess:
                    await borg.send_message(Config.PRIVATE_GROUP_ID, "`A Waifu Appeared By Was Unable To Reverse Search Image! Sorry :(`")
                    return
                await borg.send_message(event.chat_id, f"/protecc {guess}")
                await borg.send_message(Config.PRIVATE_GROUP_ID, f"A {guess} Waifu Appeard At {event.chat_id} \n**Catch Success!**")
