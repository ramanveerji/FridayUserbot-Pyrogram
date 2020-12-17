from telethon.utils import pack_bot_file_id
from telethon import Button, custom, events, functions
from fridaybot.modules.sql_helper.channel_sticker_sql import (
    add_new_data_in_db,
    is_data_indb,
    remove_data,
)
from fridaybot.utils import admin_cmd

@friday.on(admin_cmd(pattern="scs$"))
async def _m(event):
    await event.edit("`Processing..`")
    id_s = event.chat_id
    lmao = await event.get_reply_message()
    if not lmao.sticker and lmao.sticker.mime_type == "image/webp":
        await event.edit("`Only Sticker Allowded.`")
        return
    if is_data_indb(id_s):
        await event.edit(
            "`This Channel Sticker Data Is Already In Db, Remove First To Update it.`"
        )
        return
    elif not is_data_indb(id_s):
        bot_api_file_id = pack_bot_file_id(lmao.media)
        add_new_data_in_db(id_s, bot_api_file_id)
        await event.edit(
            "`This Sticker Has Been Set As Channel Sticker For This Channel`"
        )


@friday.on(admin_cmd(pattern="rcs$"))
async def _m(event):
    await event.edit("`Processing..`")
    id_s = event.chat_id
    if is_data_indb(id_s):
        remove_data(id_s)
        await event.edit("`Done !`")
    elif not is_data_indb(id_s):
        await event.edit("`You Need To Set Channel Sticker To Remove It`")


@friday.on(admin_cmd(pattern="ccs$"))
async def _m(event):
    await event.edit("`Processing..`")
    id_s = event.chat_id
    if is_data_indb(id_s):
        await event.edit(
            f"Yes, Channel Sticker Has Been Set. Sticker ID : {is_data_indb(id_s)}"
        )
    elif not is_data_indb(id_s):
        await event.edit("`No Channel Sticker Set For This Channel.`")


@bot.on(events.NewMessage)
async def lul(event):
    lsb = event.chat_id
    if is_data_indb(event.chat_id):
        try:
            await borg.send_file(event.chat_id, is_data_indb(event.chat_id))
        except:
            await borg.send_message(
                Config.PRIVATE_GROUP_ID, f"Failed, To Send Sticker in {lsb}"
            )
            return
    elif not is_data_indb(id_s):
        return
