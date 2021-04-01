# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

bot = db_x["BOT_USERS"]

def add_user(user_id):
    bot.insert_one({"user_id": user_id})

def check_user(user_id):
    Lol = bot.find_one({"user_id": user_id})
    if Lol:
        return True
    else:
        return False

def get_all_users():
    Lol = bot.find()
    return Lol



