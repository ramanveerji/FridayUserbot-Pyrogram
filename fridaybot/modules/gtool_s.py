from fridaybot.function import get_all_admin_chats
from fridaybot.modules.sql_helper import gban_sql
from fridaybot.utils import friday_on_cmd
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
    MessageMediaPhoto,
)
from telethon.errors import (
    BadRequestError,
    ChatAdminRequiredError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
    UserAdminInvalidError,
)
from telethon.errors.rpcerrorlist import MessageTooLongError, UserIdInvalidError
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)


@friday.on(friday_on_cmd(pattern='gbn (.*)'))
async def gbun(event):
    await event.edit("**GBanning User**")
    sucess = 0
    bad = 0
    user, reason = await get_user_from_event(event)
    if not user:
        await event.edit("`Mention A User To Gban`")
        return
    if not reason:
        hmm_r = "#GBanned"
    elif reason:
        hmm_r = reason
    if user == bot.uid:
        await event.edit("**I Can't Gban You Master :(**")
        return
    if gban_sql.is_banned:
        await event.edit("**This User Is Already Gbanned. No Point In Gbanning Him Again !**")
        return
    gban_sql.gban_user(user, hmm_r)
    chat_s = await get_all_admin_chats(event)
    len_s = len(chat_s)
    await event.edit(f"**GBanning !** [{user.first_name}](tg://user?id={user.id}) **in {len_s} Chats!**")
    for stark_s in chat_s:
        try:
          await event.client.edit_permissions(stark_s, user, view_messages=False)
          sucess += 1
        except:
          bad += 0
    await event.edit(f"**GBanned !**[{user.first_name}](tg://user?id={user.id}) **in {len_s} Chats!**")
    
          	
@friday.on(friday_on_cmd(pattern='ungbn (.*)'))
async def ungbun(event):
    await event.edit("**Un-GBanning User**")
    sucess = 0
    bad = 0
    user, reason = await get_user_from_event(event)
    if not user:
        await event.edit("`Mention A User To Un-Gban`")
        return
    if user == bot.uid:
        await event.edit("**I Can't Un-Gban You Master :(**")
        return
    if not gban_sql.is_banned:
        await event.edit("**This User Is Not Gbanned. No Point In Un-Gbanning Him Again !**")
        return
    gban_sql.ungban_user(user)
    chat_s = await get_all_admin_chats(event)
    len_s = len(chat_s)
    await event.edit(f"**Un-GBanning !** [{user.first_name}](tg://user?id={user.id}) **in {len_s} Chats!**")
    for stark_s in chat_s:
        try:
          await event.client.edit_permissions(stark_s, user, view_messages=True)
          sucess += 1
        except:
          bad += 0
    await event.edit(f"**Un-GBanned !**[{user.first_name}](tg://user?id={user.id}) **in {len_s} Chats!**")


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return user_obj, extra


async def get_user_sender_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj
