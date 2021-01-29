import asyncio
import os

import wget
from youtubesearchpython import SearchVideos
import asyncio
import math
import os
import time

from telethon.tl.types import DocumentAttributeAudio
from uniborg.util import edit_or_reply, friday_on_cmd, sudo_cmd
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)
from fridaybot.funtion import progress, humanbytes, time_formatter
from fridaybot.function.FastTelethon import upload_file
from fridaybot import CMD_HELP
from fridaybot.Configs import Config
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd(pattern="ytmusic ?(.*)"))
@friday.on(sudo_cmd(pattern="ytmusic ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    myself_stark = await edit_or_reply(
        event, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    if not os.path.isdir("./music/"):
        os.makedirs("./music/")
    path = Config.TMP_DOWNLOAD_DIRECTORY
    sedlyf = wget.download(kekme, out=path)
    opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "480",
                }
            ],
            "outtmpl": "%(title)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
    except Exception as e:
        await event.edit(f"**Failed To Download** \n**Error :** `{str(e)}`")
        return
    file_stark = f"{ytdl_data['title']}.mp3"
    lol_m = await upload_file(
            file_name=file_stark,
            client=borg,
            file=open(file_stark, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading Your Song!", file_stark
                )
            ),
        )
    capy = f"**Song Name ➠** `{thum}` \n**Requested For ➠** `{urlissed}` \n**Channel ➠** `{thums}` \n**Link ➠** `{mo}`"
    await borg.send_file(
        event.chat_id,
        lol_m,
        force_document=False,
        allow_cache=False,
        caption=capy,
        thumb=sedlyf,
        attributes=[
                DocumentAttributeAudio(
                    duration=int(ytdl_data["duration"]),
                    title=str(ytdl_data["title"]),
                    performer=str(ytdl_data["uploader"]),
                )
            ],
        supports_streaming=True,
    )
    await myself_stark.edit("`Song Uploaded. By (C) @FridayOT`")
    for files in (sedlyf, km):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "ytmusic": "**Ytmusic**\
\n\n**Syntax : **`.ytmusic <song name>`\
\n**Usage :** Downloads songs from ytmusic"
    }
)
