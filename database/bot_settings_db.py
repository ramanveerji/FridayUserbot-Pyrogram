# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

bsdb = db_x["bot_sdb"]

default_text = """<b>Hello, {user_firstname}!
This is A UserBot Of {boss_firstname}.</b>
<i>My Master is Busy As For Now, You Can Wait For Sometime
If He Needs To Talk To You, He Will Approve You!</i>

<b><u>You Have {warns} Of Warns.</b></u>
"""

default_thumb = "https://icon-icons.com/downloadimage.php?id=106660&root=1527/PNG/512/&file=shield_106660.png"


def add_pm_text(text=default_text):
    ujwal = bsdb.find_one({"_id": "PM_START_MSG"})
    if ujwal:
        bsdb.update_one({"_id": "PM_START_MSG"}, {"$set": {"pm_msg": text}})
    else:
        bsdb.insert_one({"_id": "PM_START_MSG", "pm_msg": text})


def add_pm_thumb(thumb=default_thumb):
    ujwal = bsdb.find_one({"_id": "PM_START_THUMB"})
    if ujwal:
        bsdb.update_one({"_id": "PM_START_THUMB"}, {"$set": {"pm_img": text}})
    else:
        bsdb.insert_one({"_id": "PM_START_THUMB", "pm_img": text})


def get_thumb():
    ujwal = bsdb.find_one({"_id": "PM_START_THUMB"})
    if ujwal:
        return ujwal["pm_img"]
    else:
        return default_thumb


def get_pm_text():
    ujwal = bsdb.find_one({"_id": "PM_START_MSG"})
    if ujwal:
        return ujwal["pm_msg"]
    else:
        return default_text


def set_chat_bot_setting(settin=False):
    meisnub = bsdb.find_one({"_id": "CHAT_BOT_S"})
    if meisnub:
        bsdb.update_one({"_id": "CHAT_BOT_S"}, {"$set": {"chat_bot": settin}})
    else:
        bsdb.insert_one({"_id": "CHAT_BOT_S", "chat_bot": settin})


def get_chatbot_setting():
    ujwal = bsdb.find_one({"_id": "CHAT_BOT_S"})
    if ujwal:
        return ujwal["chat_bot"]
    else:
        return True


def set_pm_spam_limit(psl=3):
    stark = bsdb.find_one({"_id": "LIMIT_PM"})
    if stark:
        bsdb.update_one({"_id": "LIMIT_PM"}, {"$set": {"psl": psl}})
    else:
        bsdb.insert_one({"_id": "LIMIT_PM", "psl": psl})


def get_pm_spam_limit():
    meisnub = bsdb.find_one({"_id": "LIMIT_PM"})
    if meisnub:
        return meisnub["psl"]
    else:
        return 3


def pm_permit_should_work(sw=True):
    die = bsdb.find_one({"_id": "PM"})
    if die:
        bsdb.update_one({"_id": "PM"}, {"$set": {"pm_s": sw}})
    else:
        bsdb.insert_one({"_id": "PM", "pm_s": sw})


def get_pm_setting_s():
    stark = bsdb.find_one({"_id": "PM"})
    if stark:
        return stark["pm_s"]
    else:
        return True


# def add_black_list_chat(chat_id):
#   black_list_find = bsdb.find_one({"_id": "BLC"})
