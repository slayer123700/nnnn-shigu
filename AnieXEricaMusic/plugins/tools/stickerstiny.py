import os
import cv2
from PIL import Image
from pyrogram import Client, filters
from AnieXEricaMusic import app

@app.on_message(filters.command("tiny"))
async def tiny_sticker(client, message):
    reply = message.reply_to_message
    if not (reply and reply.sticker):
        await message.reply("ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ! 👀")
        return
    kontol = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ! 🕊️")
    await kontol.edit_text("❤️")
    
    try:
        ik = await app.download_media(reply)
        if not ik:
            await message.reply("ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ ᴍᴇᴅɪᴀ.")
            return
    except Exception as e:
        await message.reply(f"Error downloading media: {str(e)}")
        return
    
    im1 = Image.open("AnieXEricaMusic/assets/tiny.png")
    
    if ik.endswith(".tgs"):
        try:
            await app.download_media(reply, "wel2.tgs")
            os.system("lottie_convert.py wel2.tgs json.json")
            with open("json.json", "r") as json_file:
                jsn = json_file.read()
                jsn = jsn.replace("512", "2000")
            with open("json.json", "w") as json_file:
                json_file.write(jsn)
            os.system("lottie_convert.py json.json wel2.tgs")
            file = "wel2.tgs"
            os.remove("json.json")
        except Exception as e:
            await message.reply(f"Error during Lottie conversion: {str(e)}")
            return
    elif ik.endswith((".gif", ".mp4")):
        try:
            iik = cv2.VideoCapture(ik)
            _, busy = iik.read()
            cv2.imwrite("i.png", busy)
            fil = "i.png"
            im = Image.open(fil)
            z, d = im.size
            if z == d:
                xxx, yyy = 200, 200
            else:
                t = z + d
                a = z / t
                b = d / t
                aa = (a * 100) - 50
                bb = (b * 100) - 50
                xxx = 200 + 5 * aa
                yyy = 200 + 5 * bb
            k = im.resize((int(xxx), int(yyy)))
            k.save("k.png", format="PNG", optimize=True)
            im2 = Image.open("k.png")
            back_im = im1.copy()
            back_im.paste(im2, (150, 0))
            back_im.save("o.webp", "WEBP", quality=95)
            file = "o.webp"
            os.remove(fil)
            os.remove("k.png")
        except Exception as e:
            await message.reply(f"Error processing video: {str(e)}")
            return
    else:
        try:
            im = Image.open(ik)
            z, d = im.size
            if z == d:
                xxx, yyy = 200, 200
            else:
                t = z + d
                a = z / t
                b = d / t
                aa = (a * 100) - 50
                bb = (b * 100) - 50
                xxx = 200 + 5 * aa
                yyy = 200 + 5 * bb
            k = im.resize((int(xxx), int(yyy)))
            k.save("k.png", format="PNG", optimize=True)
            im2 = Image.open("k.png")
            back_im = im1.copy()
            back_im.paste(im2, (150, 0))
            back_im.save("o.webp", "WEBP", quality=95)
            file = "o.webp"
            os.remove("k.png")
        except Exception as e:
            await message.reply(f"Error processing image: {str(e)}")
            return
    
    await app.send_document(message.chat.id, file, reply_to_message_id=message.id)
    
    await kontol.delete()
    
    if os.path.exists(file):
        os.remove(file)
    if os.path.exists(ik):
        os.remove(ik)
