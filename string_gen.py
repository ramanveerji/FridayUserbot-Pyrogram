import pyrogram
from pyrogram import Client

api_id = input("Enter Your API ID.")
api_hash = input("Enter Your API HASH.")

with Client("FridayUB", api_id=api_id, api_hash=api_hash) as bot_:
    first_name = (bot_.get_me()).first_name
    string_session_ = f"<b>String Session For {first_name}</b> \n<code>{bot_.export_session_string()}</code>"
    bot_.send_message("me", string_session_, parse_mode="html")
    print("<<! Please Check Saved Message For STRINGSESSION !>>")
