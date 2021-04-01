# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

gmuteh = db_x["GMUTE"]


def is_gmuted(sender_id):
    kk = gmuteh.find_one({"sender_id": sender_id})
    if not kk:
        return False
    else:
        return True


def gmute(sender_id, reason="#GMuted"):
    gmuteh.insert_one({"sender_id": sender_id, "reason": reason})


def ungmute(sender_id):
    gmuteh.delete_one({"sender_id": sender_id})
