from datetime import datetime
from pyrogram.enums import ParseMode
from pyrogram import filters
from pyrogram.types import Message

from AnieXEricaMusic import app
from AnieXEricaMusic.core.call import AMBOT
from AnieXEricaMusic.utils import bot_sys_stats
from AnieXEricaMusic.utils.decorators.language import language
from AnieXEricaMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL

LORD_ID = 6018803920

@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    user = message.from_user
    user_firstname = f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
    bot_private_link = f"<a href='tg://user?id={app.me.id}'>.𝑲𝒚𝒐𝒖𝒌𝒐 𝑴𝒖𝒔𝒊𝒄"
    lord_firstname = f"<a href='tg://user?id={6018803920}'>S L A Y E R</a>"

    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )

    pytgping = await AMBOT.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000

    if user.id == LORD_ID:
        ping_2_message = (
            f"🔱 I'ᴍ ᴀʟɪᴠᴇ ᴍʏ ʟᴏʀᴅ\n\n"
            f" ➣ ɪ'ᴍ {bot_private_link}\n"
            f" ➣ ᴄʀᴇᴀᴛᴏʀ ⌯ {lord_firstname}\n"
            f"┏━━━━━━━━━━━━━⧫\n"
            f"┠ ➥ Uᴘᴛɪᴍᴇ : {UP}\n"
            f"┠ ➥ Rᴀᴍ : {RAM}%\n"
            f"┠ ➥ ᴄᴘᴜ : {CPU}%\n"
            f"┠ ➥ ᴅɪsᴋ : {DISK}%\n"
            f"┠ ➥ ᴘʏ - ᴛɢᴄᴀʟʟs : <code>{resp}ᴍs</code>\n"
            f"┗━━━━━━━━━━━━━━⧫"
        )
    else:
        ping_2_message = (
            f"ʏᴏᴏ ! {user_firstname}\n\n"
            f"➣ ɪ'ᴍ {bot_private_link}\n"
            f"➣ ᴄʀᴇᴀᴛᴏʀ ⌯ {lord_firstname}\n"
            f"┏━━━━━━━━━━━━━⧫\n"
            f"┠ ➥ Uᴘᴛɪᴍᴇ : {UP}\n"
            f"┠ ➥ Rᴀᴍ : {RAM}%\n"
            f"┠ ➥ ᴄᴘᴜ : {CPU}%\n"
            f"┠ ➥ ᴅɪsᴋ : {DISK}%\n"
            f"┠ ➥ ᴘʏ - ᴛɢᴄᴀʟʟs : <code>{resp}ᴍs</code>\n"
            f"┗━━━━━━━━━━━━━━⧫"
        )

    await response.edit_text(
        ping_2_message.format(UP, RAM, CPU, DISK, resp, pytgping),
        parse_mode=ParseMode.HTML,
        reply_markup=supp_markup(_),
    )
