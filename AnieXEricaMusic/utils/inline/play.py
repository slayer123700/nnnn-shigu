
import math
import random
from pyrogram.types import InlineKeyboardButton
import config
from AnieXEricaMusic.utils.formatters import time_to_seconds
from AnieXEricaMusic import app

def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons



def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        ba = "▰▱▱▱▱▱▱▱▱"
    elif 10 < umm < 20:
        ba = "▰▰▱▱▱▱▱▱▱"
    elif 20 <= umm < 30:
        ba = "▰▰▰▱▱▱▱▱▱"
    elif 30 <= umm < 40:
        ba = "▰▰▰▰▱▱▱▱▱"
    elif 40 <= umm < 50:
        ba = "▰▰▰▰▰▱▱▱▱"
    elif 50 <= umm < 60:
        ba = "▰▰▰▰▰▰▱▱▱"
    elif 60 <= umm < 70:
        ba = "▰▰▰▰▰▰▰▱▱"
    elif 70 <= umm < 80:
        ba = "▰▰▰▰▰▰▰▰▱"
    elif 80 <= umm < 95:
        ba = "▰▰▰▰▰▰▰▰▰"
    else:
        ba = "▰▰▰▰▰▰▰▰▰▰"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {ba} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="ʀᴇꜱᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton("𝚈𝚝 𝙰𝚙𝚒", callback_data="bot_info_data"),
            InlineKeyboardButton(text="ᴘᴀᴜꜱᴇ", callback_data=f"ADMIN Pause|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="ꜱᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="ꜱᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="ᴇɴᴅ 🍁", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
         InlineKeyboardButton(text=_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true",)
        ],
        [
            InlineKeyboardButton(text="ʀᴇꜱᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ᴘᴀᴜꜱᴇ", callback_data=f"ADMIN Pause|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="ꜱᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="ꜱᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AMBOTPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AMBOTPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
