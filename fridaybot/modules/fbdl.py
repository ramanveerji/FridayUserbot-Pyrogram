#    Copyright (C) @chsaiujwal 2020-2021
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

from datetime import datetime
import requests
import re
import html
import os
from fridaybot import CMD_HELP, sclient
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd, admin_cmd

fridaythumb = "./resources/IMG_20200929_103719_628.jpg"


def main(url, filename):
    try:
        download_video("HD", url, filename)
    except(KeyboardInterrupt):
        download_video("SD", url, filename)


def download_video(quality, url, filename):
    html = requests.get(url).content.decode('utf-8')
    video_url = re.search(rf'{quality.lower()}_src:"(.+?)"', html).group(1)
    file_size_request = requests.get(video_url, stream=True)
    file_size = int(file_size_request.headers['Content-Length'])
    block_size = 1024
    with open(filename + '.mp4', 'wb') as f:
        for data in file_size_request.iter_content(block_size):
            f.write(data)
    print("\nVideo downloaded successfully.")


@friday.on(admin_cmd(pattern="fbdl (.*)"))
async def _(event):
    if event.fwd_from:
        return
    url = event.pattern_match.group(1)
    x = re.match(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com', url)

    if x:
        html = requests.get(url).content.decode('utf-8')
    else:
        await event.edit("This Video Is Either Private Or URL Is Invalid. Exiting... ")
        return

    _qualityhd = re.search('hd_src:"https', html)
    _qualitysd = re.search('sd_src:"https', html)
    _hd = re.search('hd_src:null', html)
    _sd = re.search('sd_src:null', html)

    list = []
    _thelist = [_qualityhd, _qualitysd, _hd, _sd]
    for id,val in enumerate(_thelist):
        if val != None:
            list.append(id)
    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')

    main(url, filename)
    await event.edit("Video Downloaded Successfully. Starting To Upload.")
        
    kk = f"{filename}.mp4"
    caption= f"Facebook Video Successfully by Fridaybot.\nGet Your Fridaybot From @Fridayot."
        
    await borg.send_message(
      event.chat_id,
      caption,
      thumb=fridaythumb,
      parse_mode="HTML",
      file=kk,
      force_document=True,
      allow_cache=False,
    )
    os.system(f"rm {kk}")


CMD_HELP.update(
    {
        "facebookDL": "**Facebook Video Downloader**\
\n\n**Syntax : **`.fbdl <video-link>`\
\n**Usage :** Downlosds The Facebook Video."
    }
)
