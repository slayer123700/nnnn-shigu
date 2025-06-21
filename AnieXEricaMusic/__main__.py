import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AnieXEricaMusic import LOGGER, app, userbot
from AnieXEricaMusic.core.call import AMBOT
from AnieXEricaMusic.misc import sudo
from AnieXEricaMusic.plugins import ALL_MODULES
from AnieXEricaMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        return  # Instead of exiting, return from the function if client variables aren't set
    
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER(__name__).warning(f"Error while loading banned users: {str(e)}")

    await app.start()
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("AnieXEricaMusic.plugins" + all_module)
        except Exception as e:
            LOGGER(__name__).warning(f"Error importing module {all_module}: {str(e)}")

    LOGGER("AnieXEricaMusic.plugins").info("Successfully Imported Modules...")

    await userbot.start()
    await AMBOT.start()
    
    try:
        await AMBOT.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("AnieXEricaMusic").warning(
            "Please turn on the videochat of your log group/channel.\n\nContinuing without video..."
        )
    except Exception as e:
        LOGGER("AnieXEricaMusic").warning(f"Error starting AMBOT stream: {str(e)}")

    try:
        await AMBOT.decorators()
    except Exception as e:
        LOGGER("AnieXEricaMusic").warning(f"Error applying decorators: {str(e)}")

    LOGGER("AnieXEricaMusic").info(
        "\x41\x6E\x69\x65\x58\x45\x72\x69\x63\x61\x20\x4D\x75\x73\x69\x63\x20\x42\x6F\x74\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6C\x6C\x79\x2E\x5C\x6E\x5C\x6E\x44\x6F\x6E\x27\x74\x20\x66\x6F\x72\x67\x65\x74\x20\x74\x6F\x20\x4A\x6F\x69\x6E\x20\x40\x41\x4D\x42\x4F\x54\x59\x54"
    )

    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AnieXEricaMusic").info("Stopping AnieXEricaMusic Bot...")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
