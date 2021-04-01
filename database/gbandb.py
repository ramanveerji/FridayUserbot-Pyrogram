# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

gbun = db_x["GBAN"]


def gban_user(user, reason="#GBanned"):
    gbun.insert_one({"user": user, "reason": reason})


def ungban_user(user):
    gbun.delete_one({"user": user})


def gban_list():
    return list(gbun.find({}))


def gban_info(user):
    kk = gbun.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]
