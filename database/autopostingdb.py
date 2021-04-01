# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

autoposter = db_x["AutoPoster"]


def add_new_autopost(to_channel, target_channel):
    autoposter.insert_one(
        {"target_channel": int(target_channel), "to_channel": int(to_channel)}
    )


def check_if_autopost_in_db(to_channel, target_channel):
    st = autoposter.find_one(
        {"target_channel": int(target_channel), "to_channel": int(to_channel)}
    )
    if st:
        return True
    else:
        return False


def del_autopost(to_channel, target_channel):
    autoposter.delete_one(
        {"target_channel": int(target_channel), "to_channel": int(to_channel)}
    )


def get_autopost(target_channel):
    sed = autoposter.find({"target_channel": int(target_channel)})
    return list(sed)
