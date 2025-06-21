
import requests
from telegraph import Telegraph
from pyrogram import Client, filters
from pyrogram.types import Message
import os
from AnieXEricaMusic import app
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup
from config import config 

class Upload:
    def __init__(self):
        self.catbox_url = "https://catbox.moe/user/api.php"
        self.telegraph = Telegraph()
        self.telegraph.create_account(short_name="UploaderBot")

    def upload_to_catbox(self, file_path):
        with open(file_path, 'rb') as file:
            data = {'reqtype': 'fileupload'}
            files = {'fileToUpload': file}
            response = requests.post(self.catbox_url, data=data, files=files)
        
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to upload file. Status code: {response.status_code}"
    def upload_text_to_telegraph(self, title, content):
        response = self.telegraph.create_page(
            title=title,
            html_content=content
        )
        return f"https://telegra.ph/{response['path']}"

uploader = Upload()

# /tgm command: Reply to an image or video and upload to catbox
@app.on_message(filters.command("tgm" , prefixes=config.COMMAND_PREFIXES) & filters.reply)
async def upload_to_catbox(client: Client, message: Message):

    if not (message.reply_to_message.photo or message.reply_to_message.video or message.reply_to_message.audio):
        await message.reply("𝖯𝗅𝖾𝖺𝗌𝖾 𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺𝗇 𝗂𝗆𝖺𝗀𝖾 , 𝗏𝗂𝖽𝖾𝗈 𝗈𝗋 𝖺𝗎𝖽𝗂𝗈.")
        return

    a = await message.reply_text("𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽𝗂𝗇𝗀 𝖳𝗁𝖾 𝖥𝗂𝗅𝖾...")

    file_path = await message.reply_to_message.download()

    try:
        await a.edit_text("𝖳𝗋𝗒𝗂𝗇𝗀 𝖳𝗈 𝖴𝗉𝗅𝗈𝖺𝖽 𝖳𝗈 𝖳𝗁𝖾 𝖠𝖯𝖨....")
        catbox_link = uploader.upload_to_catbox(file_path)
        link = f"https://telegram.me/share/url?url={catbox_link}"
        
        share_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔗 𝖲𝗁𝖺𝗋𝖾 𝖫𝗂𝗇𝗄", url=link)]]
        )
        await a.edit_text(f"**𝖥𝗂𝗅𝖾 𝗎𝗉𝗅𝗈𝖺𝖽𝖾𝖽 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒**: [𝖫𝗂𝗇𝗄]({catbox_link})", disable_web_page_preview=True, reply_markup=share_button)
    except Exception as e:
        await message.reply(f"𝖥𝖺𝗂𝗅𝖾𝖽 𝗍𝗈 𝗎𝗉𝗅𝗈𝖺𝖽 𝗍𝗁𝖾 𝖿𝗂𝗅𝖾: {str(e)}")
    finally:
        os.remove(file_path)

@app.on_message(filters.command("tgt" , prefixes=config.COMMAND_PREFIXES))
async def upload_to_telegraph(client: Client, message: Message):
    if message.reply_to_message and message.reply_to_message.text:
        content = message.reply_to_message.text
    elif len(message.command) > 1:
        content = message.text.split(" ", 1)[1]
    else:
        await message.reply("𝖯𝗅𝖾𝖺𝗌𝖾 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝗈𝗋 𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗍𝖾𝗑𝗍 𝗍𝗈 𝗎𝗉𝗅𝗈𝖺𝖽 𝗂𝗍 𝗍𝗈 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗉𝗁.")
        return

    try:
        a = await message.reply_text("𝖳𝗋𝗒𝗂𝗇𝗀 𝖳𝗈 𝖴𝗉𝗅𝗈𝖺𝖽 𝖳𝗈 𝖳𝗁𝖾 𝖠𝖯𝖨...s")
        title = f"Uploaded by {message.from_user.first_name}"
        telegraph_link = uploader.upload_text_to_telegraph(title, content)
        link = f"https://telegram.me/share/url?url={telegraph_link}"
        
        share_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔗 𝖲𝗁𝖺𝗋𝖾 𝖫𝗂𝗇𝗄", url=link)]]
        )
        await a.edit_text(f"**𝖳𝖾𝗑𝗍 𝗎𝗉𝗅𝗈𝖺𝖽𝖾𝖽 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒 **: [𝖫𝗂𝗇𝗄]({telegraph_link})", disable_web_page_preview=True , reply_markup=share_button)
    except Exception as e:
        await message.reply(f"𝖥𝖺𝗂𝗅𝖾𝖽 𝗍𝗈 𝗎𝗉𝗅𝗈𝖺𝖽 𝗍𝖾𝗑𝗍 : {str(e)}")
        

__module__ = "𝖴𝗉𝗅𝗈𝖺𝖽𝖾𝗋"


__help__ = """**𝖴𝗉𝗅𝗈𝖺𝖽𝖾𝗋 𝖡𝗈𝗍 𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌:**

- **𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌:**

 ✧ `/𝗍𝗀𝗆` : 𝖱𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺𝗇 𝗂𝗆𝖺𝗀𝖾, 𝖺𝗇𝖽 𝗍𝗁𝖾 𝖻𝗈𝗍 𝗐𝗂𝗅𝗅 𝗎𝗉𝗅𝗈𝖺𝖽 𝗂𝗍 𝗍𝗈 𝖢𝖺𝗍𝖻𝗈𝗑 𝖺𝗇𝖽 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝖺 𝗌𝗁𝖺𝗋𝖺𝖻𝗅𝖾 𝗅𝗂𝗇𝗄.
 
 ✧ `/𝗍𝗀𝗍` : 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝗈𝗋 𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗍𝖾𝗑𝗍 𝗆𝖾𝗌𝗌𝖺𝗀𝖾, 𝖺𝗇𝖽 𝗍𝗁𝖾 𝖻𝗈𝗍 𝗐𝗂𝗅𝗅 𝗎𝗉𝗅𝗈𝖺𝖽 𝗂𝗍 𝗍𝗈 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗉𝗁 𝖺𝗇𝖽 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝖺 𝗌𝗁𝖺𝗋𝖺𝖻𝗅𝖾 𝗅𝗂𝗇𝗄.
 
- **𝖴𝗌𝖺𝗀𝖾:**

   𝟣. **𝖨𝗆𝖺𝗀𝖾 𝖴𝗉𝗅𝗈𝖺𝖽:**
      - 𝖱𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺𝗇 𝗂𝗆𝖺𝗀𝖾 𝗎𝗌𝗂𝗇𝗀 𝗍𝗁𝖾 `/𝗍𝗀𝗆` 𝖼𝗈𝗆𝗆𝖺𝗇𝖽.
       - 𝖳𝗁𝖾 𝖻𝗈𝗍 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽𝗌 𝗍𝗁𝖾 𝗂𝗆𝖺𝗀𝖾 𝖺𝗇𝖽 𝗎𝗉𝗅𝗈𝖺𝖽𝗌 𝗂𝗍 𝗍𝗈 𝗍𝗁𝖾 𝖢𝖺𝗍𝖻𝗈𝗑 𝖠𝖯𝖨.
       - 𝖠 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗍𝗁𝖾 𝗎𝗉𝗅𝗈𝖺𝖽𝖾𝖽 𝗂𝗆𝖺𝗀𝖾 𝗂𝗌 𝗋𝖾𝗍𝗎𝗋𝗇𝖾𝖽 𝖺𝗅𝗈𝗇𝗀 𝗐𝗂𝗍𝗁 𝖺 𝗌𝗁𝖺𝗋𝖾 𝖻𝗎𝗍𝗍𝗈𝗇.
 
   𝟤. **𝖳𝖾𝗑𝗍 𝖴𝗉𝗅𝗈𝖺𝖽:**
      - 𝖴𝗌𝖾 `/𝗍𝗀𝗍 <𝗍𝖾𝗑𝗍>` 𝗈𝗋 𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗍𝖾𝗑𝗍 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗐𝗂𝗍𝗁 `/𝗍𝗀𝗍`.
       - 𝖳𝗁𝖾 𝖻𝗈𝗍 𝗎𝗉𝗅𝗈𝖺𝖽𝗌 𝗍𝗁𝖾 𝗉𝗋𝗈𝗏𝗂𝖽𝖾𝖽 𝗍𝖾𝗑𝗍 𝗍𝗈 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗉𝗁.
       - 𝖠 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗍𝗁𝖾 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗉𝗁 𝗉𝖺𝗀𝖾 𝗂𝗌 𝗋𝖾𝗍𝗎𝗋𝗇𝖾𝖽 𝖺𝗅𝗈𝗇𝗀 𝗐𝗂𝗍𝗁 𝖺 𝗌𝗁𝖺𝗋𝖾 𝖻𝗎𝗍𝗍𝗈𝗇.
 """
