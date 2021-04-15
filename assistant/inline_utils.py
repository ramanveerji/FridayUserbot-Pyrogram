# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

import logging
import re
import string
from random import choice

import requests
from bs4 import BeautifulSoup
from pyrogram import __version__, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InputTextMessageContent,
)
from tinydb import Query, TinyDB

from main_startup import CMD_LIST, XTRA_CMD_LIST, Friday, bot, friday_version
from main_startup.config_var import Config
from main_startup.helper_func.basic_helpers import (
    cb_wrapper,
    get_all_pros,
    inline_wrapper,
    paginate_help,
)

db_m = TinyDB("./main_startup/Cache/secret.json")
db_s = TinyDB("./main_startup/Cache/not4u.json")


@bot.on_inline_query()
@inline_wrapper
async def owo(client, inline_query):
    string_given = inline_query.query.lower()
    if "modapk" in inline_query.query.lower():
        if not " " in inline_query.query.lower():
            return
        string_given = inline_query.query.lower()
        sgname = string_given.split(" ", maxsplit=1)[1]
        print(sgname)
        PabloEscobar = (
            f"https://an1.com/tags/MOD/?story={sgname}&do=search&subaction=search"
        )
        r = requests.get(PabloEscobar)
        results = []
        soup = BeautifulSoup(r.content, "html5lib")
        mydivs = soup.find_all("div", {"class": "search-results"})
        Pop = soup.find_all("div", {"class": "title"})
        cnte = len(mydivs)
        for cnt in range(cnte):
            sucker = mydivs[cnt]
            pH9 = sucker.find("a").contents[0]
            file_name = pH9
            pH = sucker.findAll("img")
            imme = pH[0]["src"]
            Pablo = Pop[0].a["href"]
            ro = requests.get(Pablo)
            soupe = BeautifulSoup(ro.content, "html5lib")
            myopo = soupe.find_all("div", {"class": "item"})
            capt = f"**{file_name}** \n** {myopo[0].text}**\n**{myopo[1].text}**\n**{myopo[2].text}**\n**{myopo[3].text}**"
            mydis0 = soupe.find_all("a", {"class": "get-product"})
            Lol9 = mydis0[0]
            lemk = "https://an1.com" + Lol9["href"]

            results.append(
                InlineQueryResultPhoto(
                    photo_url=imme,
                    title=file_name,
                    caption=capt,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="<<! Download Link!>>",
                                    callback_data=f"apk_{lemk}",
                                ),
                            ]
                        ]
                    ),
                )
            )
        await client.answer_inline_query(inline_query.id, cache_time=0, results=results)
    elif "not4u" in string_given:
        if not ";" in string_given:
            return
        ok = string_given.split(" ", maxsplit=1)[1]
        user, msg = ok.split(";")
        fu = int(user) if user.isdigit() else user
        try:
            ui = await Friday.get_users(fu)
        except BaseException as e:
            logging.error(str(e))
            return
        owo = (
            f"@{ui.username}"
            if ui.username
            else f"[{ui.first_name}](tg://user?id={ui.id})"
        )
        chars = string.hexdigits
        randomc = "".join(choice(chars) for _ in range(4))
        stark_data = {"secret_code": randomc, "id": ui.id, "msg": msg}
        db_s.insert(stark_data)
        texts = f"Everyone Except {owo} Can Read This Message. \nClick Below To Check Message! \n**Note :** `Only He/She Can't Open It!`"
        ok_s = [
            (
                InlineQueryResultArticle(
                    title="OwO! Not For You",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="Show Message !", callback_data=f"nu_{randomc}"
                                )
                            ]
                        ]
                    ),
                    input_message_content=InputTextMessageContent(texts),
                )
            )
        ]
        await client.answer_inline_query(inline_query.id, cache_time=0, results=ok_s)
    elif "whisper" in string_given:
        if not ";" in string_given:
            return
        ok = string_given.split(" ", maxsplit=1)[1]
        user, msg = ok.split(";")
        fu = int(user) if user.isdigit() else user
        try:
            ui = await Friday.get_users(fu)
        except BaseException as e:
            logging.error(str(e))
            return
        owo = (
            f"@{ui.username}"
            if ui.username
            else f"[{ui.first_name}](tg://user?id={ui.id})"
        )
        chars = string.hexdigits
        randomc = "".join(choice(chars) for _ in range(4))
        stark_data = {"secret_code": randomc, "id": ui.id, "msg": msg}
        db_m.insert(stark_data)
        texts = f"A Whisper Has Been Sent For {owo} . \nClick Below To Check Message! \n**Note :** `Only He/She Can Open It!`"
        ok_s = [
            (
                InlineQueryResultArticle(
                    title="Ssh! This is A Secret Message",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="Show Message !", callback_data=f"sc_{randomc}"
                                )
                            ]
                        ]
                    ),
                    input_message_content=InputTextMessageContent(texts),
                )
            )
        ]
        await client.answer_inline_query(inline_query.id, cache_time=0, results=ok_s)
    elif "help" in string_given:
        total_ = len(CMD_LIST)
        bttn = [
            [
                InlineKeyboardButton(
                    text="Main Command Help", callback_data=f"make_basic_button_True"
                )
            ]
        ]
        if Config.LOAD_UNOFFICIAL_PLUGINS:
            total_ = len(XTRA_CMD_LIST) + len(CMD_LIST)
            bttn = [
                [
                    InlineKeyboardButton(
                        text="Xtra Command Help",
                        callback_data=f"make_basic_button_False",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Main Command Help",
                        callback_data=f"make_basic_button_True",
                    )
                ],
            ]
        nice_text = f"**FridayUserBot Commands** \n**Friday Version :** __{friday_version}__ \n**PyroGram Version :** __{__version__}__ \n**Total Plugins Loaded :** __{total_}__"
        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                (
                    InlineQueryResultArticle(
                        title="Help Article!",
                        reply_markup=InlineKeyboardMarkup(bttn),
                        input_message_content=InputTextMessageContent(nice_text),
                    )
                )
            ],
        )


@bot.on_callback_query(filters.regex(pattern="sc_(.*)"))
async def no_horny(client, cb):
    o = await get_all_pros()
    data_m = cb.matches[0].group(1)
    stark_moment = Query()
    sstark = db_m.search(stark_moment.secret_code == data_m)
    if sstark == []:
        await cb.answer(
            "OwO, It Seems Message Has Been Deleted From Server :(",
            cache_time=0,
            show_alert=True,
        )
        return
    id_s = sstark[0]["id"]
    o.append(int(id_s))
    if cb.from_user.id not in o:
        await cb.answer(
            "This Message Is Not For You, OwO ! Btw, This is A Bomb Making Secret.!",
            cache_time=0,
            show_alert=True,
        )
        return
    await cb.answer(sstark[0]["msg"], cache_time=0, show_alert=True)


@bot.on_callback_query(filters.regex(pattern="nu_(.*)"))
async def nothing_here(client, cb):
    data_m = cb.matches[0].group(1)
    stark_moment = Query()
    sstark = db_s.search(stark_moment.secret_code == data_m)
    if sstark == []:
        await cb.answer(
            "OwO, It Seems Message Has Been Deleted From Server :(",
            cache_time=0,
            show_alert=True,
        )
        return
    id_s = sstark[0]["id"]
    if cb.from_user.id == int(id_s):
        await cb.answer(
            "Everyone Except You Can Read This Message. Hehe!",
            cache_time=0,
            show_alert=True,
        )
        return
    await cb.answer(sstark[0]["msg"], cache_time=0, show_alert=True)


@bot.on_callback_query(filters.regex(pattern="make_basic_button_(True|False)"))
@cb_wrapper
async def wow_nice(client, cb):
    nice = True
    if cb.matches[0].group(1) == "False":
        nice = False
    if nice is False:
        v_t = XTRA_CMD_LIST
        bttn = paginate_help(0, XTRA_CMD_LIST, "helpme", is_official=nice)
    else:
        v_t = CMD_LIST
        bttn = paginate_help(0, CMD_LIST, "helpme", is_official=nice)
    await cb.edit_message_text(
        f"Command List & Help \n**Total Commands :** `{len(v_t)}` \n**(C) @FRIDAYOT**",
        reply_markup=InlineKeyboardMarkup(bttn),
    )


@bot.on_callback_query(filters.regex(pattern="cleuse"))
@cb_wrapper
async def close_it_please(client, cb):
    await cb.edit_message_text("**Closed Help Menu**!")


@bot.on_callback_query(filters.regex(pattern="backme_(.*)_(True|False)"))
@cb_wrapper
async def get_back_vro(client, cb):
    page_number = int(cb.matches[0].group(1))
    is_official = True
    if cb.matches[0].group(2) == "False":
        is_official = False
    cmd_list = CMD_LIST if is_official else XTRA_CMD_LIST
    buttons = paginate_help(page_number, cmd_list, "helpme", is_official=is_official)
    nice_text = f"**FridayUserBot Commands & Help Menu!** \n\n**Friday Version :** __{friday_version}__ \n**PyroGram Version :** __{__version__}__ \n**Total Plugins Loaded :** __{len(CMD_LIST)}__"
    await cb.edit_message_text(nice_text, reply_markup=InlineKeyboardMarkup(buttons))


@bot.on_callback_query(filters.regex(pattern="us_plugin_(.*)_(True|False)"))
@cb_wrapper
async def give_plugin_cmds(client, cb):
    plugin_name, page_number = cb.matches[0].group(1).split("|", 1)
    is_official = True
    if cb.matches[0].group(2) == "False":
        is_official = False
    cmd_list = CMD_LIST if is_official else XTRA_CMD_LIST
    help_string = f"**💡 PLUGIN NAME 💡 :** `{plugin_name}` \n{cmd_list[plugin_name]}"
    help_string += "\n\n**(C) @FRIDAYOT** ".format(plugin_name)
    await cb.edit_message_text(
        help_string,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Go Back",
                        callback_data=f"backme_{page_number}_{is_official}",
                    )
                ]
            ]
        ),
    )


@bot.on_callback_query(filters.regex(pattern="helpme_next\((.+?)\)_(True|False)"))
@cb_wrapper
async def give_next_page(client, cb):
    current_page_number = int(cb.matches[0].group(1))
    is_official = True
    if cb.matches[0].group(2) == "False":
        is_official = False
    cmd_list = CMD_LIST if is_official else XTRA_CMD_LIST
    buttons = paginate_help(
        current_page_number + 1, cmd_list, "helpme", is_official=is_official
    )
    await cb.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@bot.on_callback_query(filters.regex(pattern="helpme_prev\((.+?)\)_(True|False)"))
@cb_wrapper
async def give_old_page(client, cb):
    current_page_number = int(cb.matches[0].group(1))
    is_official = True
    if cb.matches[0].group(2) == "False":
        is_official = False
    cmd_list = CMD_LIST if is_official else XTRA_CMD_LIST
    buttons = paginate_help(
        current_page_number - 1, cmd_list, "helpme", is_official=is_official
    )
    await cb.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@bot.on_callback_query(filters.regex(pattern="apk_(.*)"))
@cb_wrapper
async def ytv_(client, cb):
    lemk = cb.matches[0].group(1)
    rr = requests.get(lemk)
    soup = BeautifulSoup(rr.content, "html5lib")
    script = soup.find("script", type="text/javascript")
    leek = re.search(r'href=[\'"]?([^\'" >]+)', script.text).group()
    dl_link = leek[5:]
    await cb.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Download Link", url=lemk)],
                [InlineKeyboardButton("Direct Download Link", url=dl_link)],
            ]
        )
    )
