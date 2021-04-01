# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

db_y = db_x["PMPERMIT"]


def approve_user(user_id):
    cd = db_y.find_one({"_id": "PmPermit"})
    if cd:
        db_y.update_one({"_id": "PmPermit"}, {"$push": {"user_id": user_id}})
    elif not cd:
        user_idc = [user_id]
        db_y.insert_one({"_id": "PmPermit", "user_id": user_idc})


def disapprove_user(user_id):
    db_y.update_one({"_id": "PmPermit"}, {"$pull": {"user_id": user_id}})


def is_user_approved(user_id):
    sm = db_y.find_one({"_id": "PmPermit"})
    if sm:
        kek = list(sm.get("user_id"))
        if user_id in kek:
            return True
        else:
            return False
    else:
        return False


def user_list():
    sm = db_y.find_one({"_id": "PmPermit"})
    if sm:
        return list(sm.get("user_id"))
    else:
        return False
