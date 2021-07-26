from database import db_x

nighttime = db_x["NIGHT_TIME"]


async def add_night_chat(chat_id):
    await nighttime.insert_one({"chat_id": chat_id})


async def rm_night_chat(chat_id):
    await nighttime.delete_one({"chat_id": chat_id})


async def get_all_night_chats():
    lol = [ujwal async for ujwal in nighttime.find({})]
    return lol


async def is_night_chat_in_db(chat_id):
    k = await nighttime.find_one({"chat_id": chat_id})
    if k:
        return True
    else:
        return False
