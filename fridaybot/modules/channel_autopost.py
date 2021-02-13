#    Copyright (C) @DevsExpo 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from fridaybot.modules.sql_helper.auto_post_sql import add_new_post_data_in_db, get_all_post_data, is_post_data_in_db, remove_post_data
from telethon import events
from telethon.utils import pack_bot_file_id

@friday.on(friday_on_cmd(pattern="autopost ?(.*)"))
async def lol(event):
    if (event.is_pvt or event.is_group):
        await event.edit("`Only Channels Can Use THis Feature.`")
        return
    sed = event.pattern_match.group(1)
    if is_post_data_in_db(event.chat_id):
        await event.edit("Ah, This Channel Is Already DB")
        return
    add_new_post_data_in_db(event.chat_id, sed)
    await event.edit(f"`Add AutoPosting To This Chat From {sed}`")
    
@friday.on(friday_on_cmd(pattern="rmautopost$"))
async def lol(event):
    if (event.is_pvt or event.is_group):
        await event.edit("`Only Channels Can Use THis Feature.`")
        return
    sed = event.pattern_match.group(1)
    if not is_post_data_in_db(event.chat_id):
        await event.edit("Ah, This Channel Is Not In DB")
        return
    remove_post_data(event.chat_id)
    await event.edit(f"`Removed AutoPosting From This Channel`")
    
@bot.on(events.NewMessage())
async def what(event):
    if not is_post_data_in_db(event.chat_id):
        return
    if event.media:
        bot_api_file_id = pack_bot_file_id(event.media)
        await bot.send_file(
                is_post_data_in_db(event.chat_id),
                file=bot_api_file_id,
                caption=event.text
            )
    elif event.text:
        await borg.send_message(
           is_post_data_in_db(event.chat_id),
           event.text
           )
