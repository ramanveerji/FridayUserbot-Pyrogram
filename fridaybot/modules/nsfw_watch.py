from telethon import functions
from fridaybot.function import get_all_admin_chats, is_admin
from fridaybot.modules.sql_helper.nsfw_watch_sql import add_nsfwatch, rmnsfwatch, get_all_nsfw_enabled_chat, is_nsfwatch_indb

@friday.on(friday_on_cmd(pattern="anw$"))
async def nsfw_watch(event):
    if not event.is_group:
        await event.edit("You Can Only Nsfw Watch in Groups.")
        return
    if not await is_admin(event, bot.uid): 
        await event.edit("`You Should Be Admin To Do This!`")
        return
    if is_nsfwatch_indb(str(event.chat_id)):
        await event.edit("`This Chat is Has Already Nsfw Watch.`")
        return
    add_nsfwatch(str(event.chat_id))
    await event.edit(f"**Added Chat {event.chat.title} With Id {event.chat_id} To Database. This Groups Nsfw Contents Will Be Deleted And Will Will Be Logged in Logger Groupp**")

@friday.on(friday_on_cmd(pattern="rmnw$"))
async def disable_nsfw(event):
    if not event.is_group:
        await event.edit("You Can Only Disable Nsfw Mode in Groups.")
        return
    if not await is_admin(event, bot.uid): 
        await event.edit("`You Should Be Admin To Do This!`")
        return
    if not is_nsfwatch_indb(str(event.chat_id)):
        await event.edit("This Chat is Has Not Enabled Nsfw Watch.")
        return
    rmnsfwatch(str(event.chat_id))
    await event.edit(f"**Removed Chat {event.chat.title} With Id {event.chat_id} From Nsfw Watch**")
    
    
