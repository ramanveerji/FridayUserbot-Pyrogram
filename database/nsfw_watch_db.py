# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

nsfw = db_x["NSFW_WATCH"]


def add_chat(chat_id):
    nsfw.insert_one({"chat_id": chat_id})


def rm_chat(chat_id):
    nsfw.delete_one({"chat_id": chat_id})


def get_all_nsfw_chats():
    lol = list(nsfw.find({}))
    return lol


def is_chat_in_db(chat_id):
    k = nsfw.find_one({"chat_id": chat_id})
    if k:
        return True
    else:
        return False
