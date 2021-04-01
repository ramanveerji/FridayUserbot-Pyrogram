# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

welcome = db_x["WELCOME"]


def add_welcome(chat_id, message_id):
    stark = welcome.find_one({"chat_id": chat_id})
    if stark:
        welcome.update_one({"chat_id": chat_id}, {"$set": {"msg_id": message_id}})
    else:
        welcome.insert_one({"chat_id": chat_id, "msg_id": message_id})


def del_welcome(chat_id):
    welcome.delete_one({"chat_id": chat_id})


def welcome_info(chat_id):
    r = welcome.find_one({"chat_id": chat_id})
    if r:
        return r
    else:
        return False
