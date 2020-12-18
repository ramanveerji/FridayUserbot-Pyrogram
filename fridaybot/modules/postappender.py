from fridaybot import CMD_HELP
from fridaybot.Configs import Config
from fridaybot.modules.sql_helper.broadcast_sql import (
    add_new_datas_in_db,
    get_all_setting_data,
    is_data_indbs,
    remove_datas,
    is_footer,
)
from fridaybot.utils import friday_on_cmd
from telethon import events
lulstark = ['.', ',', '!', "'"]
@friday.on(friday_on_cmd(pattern='scf ?(.*)'))
async def _stark(event):
    lul_id = event.chat_id
    append_text = event.pattern_match.group(1)
    is_foot = True
    if event.is_group:
        await event.edit("`No, LoL You Can't Set Channel Stickers In Groups, lol`")
        return
    if event.is_private:
        await event.edit(
            "`No, LoL You Can't Set Channel Stickers In Private Chats, lol`"
        )
        return
    if append_text == (None, ' '):
        await event.edit("`Footer Can't Be None.`")
        return
    elif is_data_indbs(lul_id):
        await event.edit('`Please Remove Old Data, To Add New One`')
        return
    elif is_data_indbs(lul_id):
        add_new_datas_in_db(lul_id, append_text, is_foot)
        await event.edit("`Sucessfully, Saved This Text. Every New Message's Footer Will Be Edited To `{append_text}`")
        
@friday.on(friday_on_cmd(pattern='sch ?(.*)'))
async def _stark(event):
    lul_id = event.chat_id
    append_text = event.pattern_match.group(1)
    is_foot = False
    if event.is_group:
        await event.edit("`No, LoL You Can't Set Channel Stickers In Groups, lol`")
        return
    if event.is_private:
        await event.edit(
            "`No, LoL You Can't Set Channel Stickers In Private Chats, lol`"
        )
        return
    if append_text == (None, ' '):
        await event.edit("Footer Can't Be None.`")
        return
    elif is_data_indbs(lul_id):
        await event.edit('`Please Remove Old Data, To Add New One`')
        return
    elif is_data_indbs(lul_id):
        add_new_datas_in_db(lul_id, append_text, is_foot)
        await event.edit("`Sucessfully, Saved This Text. Every New Message's Header Will Be Edited To `{append_text}`")
        
@bot.on(events.NewMessage)
async def luli(event):
    lsb = event.chat_id
    id_s = event.chat_id
    lol_text = event.text
    if is_data_indbs(event.chat_id):
        if any(x in lulstark for x in event.text.startswith):
              return
        if is_footer(event.chat_id):
              await event.edit(f"{lol_text} \n{is_data_indbs(event.chat_id)}")
        elif not is_footer(event.chat_id):
              await event.edit(f"{is_data_indbs(event.chat_id)} \n{lol_text}")
              
    elif not is_data_indbs(event.chat_id):
        return
