""" command: .unzip
coded by @By_Azade
code rewritten my SnapDragon7410
"""

import os
import zipfile
from datetime import datetime

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo

from fridaybot import CMD_HELP
from fridaybot.function import progress
from fridaybot.utils import friday_on_cmd

thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"
extracted = Config.TMP_DOWNLOAD_DIRECTORY + "extracted/"
if not os.path.isdir(extracted):
    os.makedirs(extracted)


@friday.on(friday_on_cmd(pattern="unzip"))
async def _(event):
    if event.fwd_from:
        return
    mone = await event.edit("Processing ...")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not event.reply_to_msg_id:
        await event.edit('`Please Reply To Zip, To Unzip It`')
        return
    replym = await event.get_reply_message()
    if replym.media.document.mime_type != "application/zip":
        await mone.edit("`Please Reply To Zip, To Unzip It.`")
        return
    if event.reply_to_msg_id:
        datetime.now()
        reply_message = await event.get_reply_message()
        try:
            downloaded_file_name = await borg.download_media(
                reply_message.media,
                Config.TMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, event, c_time, "**Downloading This Zip.**")
                ),
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
        else:
            await mone.edit("Stored the zip to `{}`.".format(downloaded_file_name))
        with zipfile.ZipFile(downloaded_file_name, "r") as zip_ref:
            zip_ref.extractall(extracted)
        filename = sorted(get_lst_of_files(extracted, []))
        # filename = filename + "/"
        await event.edit("`Unzipping now.`")
        # r=root, d=directories, f = files
        for single_file in filename:
            if os.path.exists(single_file):
                # https://stackoverflow.com/a/678242/4723940
                caption_rts = os.path.basename(single_file)
                force_document = True
                supports_streaming = False
                document_attributes = []
                if single_file.endswith((".mp4", ".mp3", ".flac", ".webm")):
                    metadata = extractMetadata(createParser(single_file))
                    duration = 0
                    width = 0
                    height = 0
                    if metadata.has("duration"):
                        duration = metadata.get("duration").seconds
                    if os.path.exists(thumb_image_path):
                        metadata = extractMetadata(createParser(thumb_image_path))
                        if metadata.has("width"):
                            width = metadata.get("width")
                        if metadata.has("height"):
                            height = metadata.get("height")
                    document_attributes = [
                        DocumentAttributeVideo(
                            duration=duration,
                            w=width,
                            h=height,
                            round_message=False,
                            supports_streaming=True,
                        )
                    ]
                try:
                    await borg.send_file(
                        event.chat_id,
                        single_file,
                        caption=f"**Current Unzip File Name :** `{caption_rts}` \n**Orginal file Path** : `{downloaded_file_name}`",
                        force_document=force_document,
                        supports_streaming=supports_streaming,
                        allow_cache=False,
                        reply_to=event.message.id,
                        attributes=document_attributes,
                    )
                except Exception as e:
                    await borg.send_message(
                        event.chat_id,
                        "{} caused `{}`".format(caption_rts, str(e)),
                        reply_to=event.message.id,
                    )
                    # some media were having some issues
                    continue
                await event.edit("`Unzipped SucessFully By @FridayOT.`")
                os.remove(single_file)
        os.remove(downloaded_file_name)


def get_lst_of_files(input_directory, output_lst):
    filesinfolder = os.listdir(input_directory)
    for file_name in filesinfolder:
        current_file_name = os.path.join(input_directory, file_name)
        if os.path.isdir(current_file_name):
            return get_lst_of_files(current_file_name, output_lst)
        output_lst.append(current_file_name)
    return output_lst


CMD_HELP.update(
    {
        "unzipfile": "**Unzip File**\
\n\n**Syntax : **`.unzip <reply to zip file>`\
\n**Usage :** Unzips given zip file."
    }
)
