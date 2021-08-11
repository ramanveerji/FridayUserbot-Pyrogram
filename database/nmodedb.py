from database import db_x

night_time = db_x["NIGHT_TIME"]


async def add_night_chat(chat_id):
    await night_time.insert_one({"chat_id": chat_id})


async def rm_night_chat(chat_id):
    await night_time.delete_one({"chat_id": chat_id})


async def get_all_night_chats():
    return [ujwal async for ujwal in night_time.find({})]


async def is_night_chat_in_db(chat_id):
    k = await night_time.find_one({"chat_id": chat_id})
    return bool(k)
