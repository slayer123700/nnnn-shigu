import uvloop

uvloop.install()
from pyromod import listen
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config
from ..logging import LOGGER


class AMBOT(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="AnieXEricaMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention
        
        try:
            await self.send_message(
                chat_id=config.LOG_GROUP_ID,
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid) as e:
            LOGGER(__name__).warning(
                "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel.\nError: {str(e)}"
            )
        except Exception as ex:
            LOGGER(__name__).warning(
                f"Bot has failed to send message to the log group/channel. Reason: {type(ex).__name__}. Error: {str(ex)}"
            )

        try:
            a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
            if a.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).warning(
                    "Please promote your bot as an admin in your log group/channel."
                )
        except Exception as ex:
            LOGGER(__name__).warning(
                f"Failed to check bot's admin status in log group/channel. Reason: {type(ex).__name__}. Error: {str(ex)}"
            )
        
        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
