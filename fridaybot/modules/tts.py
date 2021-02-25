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

import asyncio
import os
import subprocess
from datetime import datetime
from langdetect import detect
from gtts import gTTS
from googletrans import LANGUAGES
import gtts
from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd
import asyncio
import time


@friday.on(friday_on_cmd(pattern="(tts|voice|texttospeech|speech)(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    stime = time.time()
    await event.edit("`Processing...`")
    input_str = event.pattern_match.group(2)
    start = datetime.now()
    if not event.reply_to_msg_id:
        await event.reply("`Please Reply To Message To Convert To Speech!`")
        return
    reply_msg = await event.get_reply_message()
    if not reply_msg.text:
        await event.edit("`Please Reply To Text Message To Convert To Speech !`")
        return
    if input_str:
        language = input_str
    else:
        language = "en"
    text = reply_msg.raw_text   
    kk = gtts.lang.tts_langs()
    if not kk.get(language):
        await event.edit("`Unsupported Language!`")
        return
    tts = gTTS(text, lang=language)
    tts.save(f'{kk.get(language)}.ogg')
    dec = detect(text)
    etime = time.time()
    hmm_time = round(etime-stime)
    dec_s = LANGUAGES.get(dec)
    owo = f"**TTS** \n**Detected Text Language :** `{dec_s.capitalize()}` \n**Speech Text :** `{kk.get(language)}` \n**Time Taken :** `{hmm_time}s` \n__Powered By @FridayOT__"
    await friday.send_file(event.chat_id,
                          file=f'{kk.get(language)}.ogg',
                          caption=owo,
                          force_document=False,
                          allow_cache=False,
                          reply_to=reply_msg.id
       )
    await event.delete()
    os.remove(f'{kk.get(language)}.ogg')
        
       
CMD_HELP.update(
    {
        "voice": " Google Text to Speech\
\nAvailable Commands:\
\n.voice LanguageCode as reply to a message\
\n\n.voice LangaugeCode | text to speak\
"
    }
)
