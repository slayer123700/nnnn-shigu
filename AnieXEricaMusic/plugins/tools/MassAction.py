from pyrogram import Client, enums, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPermissions, Message
from AnieXEricaMusic import app
from AnieXEricaMusic.misc import SUDOERS
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from AnieXEricaMusic import app, Userbot
from AnieXEricaMusic.utils.database import get_assistant
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant, ChatAdminRequired
from pyrogram.types import Message, ChatPrivileges
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired, UserAdminInvalid, BadRequest
import datetime

# Updated mention function that returns clickable user names
def mention(user, name, mention=True):
    if mention:
        link = f"<a href='tg://user?id={user}'>{name}</a>"
    else:
        link = f"<a href='https://t.me/{user}'>{name}</a>"
    return link

def get_keyboard(command):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Yes", callback_data=f"{command}_yes"),
         InlineKeyboardButton("No", callback_data=f"{command}_no")]
    ])

@app.on_message(filters.command("unpinall"))
async def unpinall(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    owner_id = None
    async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if admin.status == enums.ChatMemberStatus.OWNER:
            owner_id = admin.user.id
            owner_AMBOT = admin.user.mention
    if user_id != owner_id and user_id not in SUDOERS:
        await message.reply_text(f"Hey {message.from_user.mention}, 'unpinall' can only be executed by the group owner {owner_AMBOT}.")
        return
    confirm_msg = await message.reply(
        f"{message.from_user.mention}, are you sure you want to unpin all messages?",
        reply_markup=get_keyboard("unpinall")
    )

@app.on_callback_query(filters.regex(r"^unpinall_(yes|no)$"))
async def handle_unpinall_callback(client: Client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    owner_id = None
    async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if admin.status == enums.ChatMemberStatus.OWNER:
            owner_id = admin.user.id
            owner_AMBOT = admin.user.mention
    if user_id != owner_id and user_id not in SUDOERS:
        await callback_query.answer("Only the group owner can confirm this action.", show_alert=True)
        return
    if callback_query.data == "unpinall_yes":
        await callback_query.message.edit("Unpinned process started...")
        bot = await app.get_chat_member(chat_id, app.me.id)
        if not bot.privileges.can_pin_messages:
            await callback_query.message.edit("I don't have permission to unpin messages in this group.")
            return
        try:
            chat = await app.get_chat(chat_id)
            pinned_message = chat.pinned_message
            unpinned = 0
            if pinned_message:
                await app.unpin_chat_message(chat_id, pinned_message.message_id)
                unpinned += 1
                await callback_query.message.edit(f"Unpinned {unpinned} message successfully.")
            else:
                await callback_query.message.edit("There are no messages to unpin.")
        except Exception as e:
            print(f"Failed to unpin message: {e}")
            await callback_query.message.edit("An error occurred while trying to unpin the message.")
    elif callback_query.data == "unpinall_no":
        await callback_query.message.edit("Unpinned process canceled.")
