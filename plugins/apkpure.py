import os
import time
import requests
from bs4 import BeautifulSoup

from main_startup.core.decorators import friday_on_cmd
from main_startup.helper_func.basic_helpers import (
    delete_or_pass,
    edit_or_reply,
    get_text,
    progress,
)
@friday_on_cmd(
    ["apk", "apkpure"],
    cmd_help={"help": "APK Downloader", "example": "{ch}apk_dl (app name)"},
)
async def giveapkbro(client, message):
    stark_m = await edit_or_reply(message, "`Please Wait!`")
    app_name = get_text(message)
    if not app_name:
        await stark_m.edit(
            "`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`"
        )
        return
    c_time = time.time()
    res = requests.get(f"https://m.apkpure.com/search?q={app_name}")
    soup = BeautifulSoup(res.text, "html.parser")
    result = soup.select(".dd")
    if not result:
        await stark_m.edit("`No App Found Matching This Result!`")
        return
    for link in result[:1]:
        s_for_name = requests.get("https://m.apkpure.com" + link.get("href"))
        sfn = BeautifulSoup(s_for_name.text, "html.parser")
        ttl = sfn.select_one("title").text
        noneed = [" - APK Download"]
        for i in noneed:
            name = ttl.replace(i, "")
            res2 = requests.get(
                "https://m.apkpure.com" + link.get("href") + "/download?from=details"
            )
            soup2 = BeautifulSoup(res2.text, "html.parser")
            result = soup2.select(".ga")
        for link in result:
            dl_link = link.get("href")
            r = requests.get(dl_link)
            with open(f"{name}@FridayOT.apk", "wb") as f:
                f.write(r.content)
    final_path = f"{name}@FridayOT.apk"
    await stark_m.edit("`Apk Downloaded To My Servers, Now Starting To Upload Here!`")
    e_time = time.time()
    hmm_time = round(e_time - c_time)
    caption_eh = f"**App Name :** `{name}` \n**Time Taken :** `{hmm_time}` \n**Uploaded Using FridayUserBot**"
    await message.reply_document(
        final_path,
        progress=progress,
        progress_args=(stark_m, c_time, f"`Uploading {name} - [APK]!`"),
        caption=caption_eh,
    )
    await stark_m.delete()
    os.remove(final_path)
