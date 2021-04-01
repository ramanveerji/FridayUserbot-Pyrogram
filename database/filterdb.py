# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

filter = db_x["FILTER"]


def add_filters(keyword, chat_id, message_id) -> None:
    stark = filter.find_one({"keyword": keyword})
    if stark:
        filter.update_one(
            {"keyword": keyword},
            {"$set": {"chat_id": chat_id, "msg_id": message_id}},
        )
    else:
        filter.insert_one(
            {"keyword": keyword, "chat_id": chat_id, "msg_id": message_id}
        )


def del_filters(keyword, chat_id):
    filter.delete_one({"keyword": keyword, "chat_id": chat_id})


def filters_info(keyword, chat_id):
    r = filter.find_one({"keyword": keyword, "chat_id": chat_id})
    if r:
        return r
    else:
        return False


def filters_del(chat_id):
    filter.delete_many({"chat_id": chat_id})


def all_filters(chat_id):
    r = list(filter.find({"chat_id": chat_id}))
    if r:
        return r
    else:
        return False
