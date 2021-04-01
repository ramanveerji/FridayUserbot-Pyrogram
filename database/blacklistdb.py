# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

blacklist = db_x["BLACKLIST"]


def add_to_blacklist(trigger, chat_id):
    blacklist.insert_one({"trigger": trigger, "chat_id": chat_id})


def del_blacklist(trigger, chat_id):
    blacklist.delete_one({"trigger": trigger, "chat_id": chat_id})


def get_chat_blacklist(chat_id):
    r = list(blacklist.find({"chat_id": chat_id}))
    if r:
        return r
    else:
        return False


def num_blacklist():
    lol = list(blacklist.find({}))
    if lol:
        return len(lol)
    else:
        False


def num_blacklist_triggers_chat(chat_id):
    r = list(blacklist.find({"chat_id": chat_id}))
    if r:
        return len(r)
    else:
        return False


def is_blacklist_in_db(chat_id, trigger):
    m = blacklist.find_one({"chat_id": chat_id, "trigger": trigger})
    if m:
        return True
    else:
        return False


def blacklists_del(chat_id):
    blacklist.delete_many({"chat_id": chat_id})
