from fridaybot.modules.sql_helper.auto_post_sql import add_new_post_data_in_db, get_all_post_data, is_post_data_in_db, remove_post_data
from telethon import events
from telethon.utils import pack_bot_file_id

@bot.on(admin_cmd(pattern="autopost ?(.*)"))
async def lol(event):
    if (event.is_private or event.is_group):
        await event.edit("`Only Channels Can Use THis Feature.`")
        return
    sed = event.pattern_match.group(1)
    if is_post_data_in_db(sed , event.chat_id):
        await event.edit("Ah, This Channel Is Already DB")
        return
    add_new_post_data_in_db(sed, event.chat_id)
    await event.edit(f"`Add AutoPosting To This Chat From {sed}`")

@bot.on(admin_cmd(pattern="rmautopost$"))
async def lol(event):
    if (event.is_private or event.is_group):
        await event.edit("`Only Channels Can Use THis Feature.`")
        return
    sed = event.pattern_match.group(1)
    if not is_post_data_in_db(sed, event.chat_id):
        await event.edit("Ah, This Channel Is Not In DB")
        return
    remove_post_data(sed , event.chat_id)
    await event.edit(f"`Removed AutoPosting From This Channel`")

@bot.on(events.NewMessage())
async def what(event):
    if event.is_private:
        return
    channels_set  = get_all_post_data(event.chat_id)
    if channels_set == []:
        return
    for chat in channels_set:
        if event.media:
            await event.client.send_file(int(chat), event.media, caption=event.text)
        elif event.message:
            await event.client.send_message(int(chat), event.message)
