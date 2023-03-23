from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton #düyməsi yoxdur.!
import pyrogram
from Config import Config
from datetime import datetime
from telethon import Button
import time
import datatime
from pyrogram import Client, filters, idle
import pyrogram
from pyrogram import Client, filters
import aiofiles
import traceback
import shutil, psutil, traceback, os
import string
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import Message
from pyrogram.types import Message, User
from telethon import TelegramClient, events
from pyrogram.types import Message

app = Client(
    "User Tag Bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

#---------------------------------------------------------------GROUP GIREKEN SALAMLAMA MSJ------------------------------------------------------------------------------#
@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`Salam` {msg.from_user.mention} `Məni` {msg.chat.title} `Qrupa əlavə etdiyiniz üçün təşəkkürlər😌` \n\n **Qruplardakı userləri tag Edmək üçün Yaradıldım.\nKömək üçün /start yazmaq kifayətdir.😍**''')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
@app.on_message(filters.command("id", "info"))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = "**𝗦Σ𝗠Δ 𝗧Δ𝗚𝗚Σ𝗥 user data İnfo:**\n"
    out_str += f" 🌐 __Qrup ID__ : `{(msg.forward_from_chat or msg.chat).id}`\n"
    out_str += f" 👤 __Kullanıcı Adı__ : {msg.from_user.first_name}\n"
    out_str += f" 💬 __Mesaj ID__ : `{msg.forward_from_message_id}`\n"
    if msg.from_user:
        out_str += f" 🆔 __Kullanıcı ID__ : `{msg.from_user.id}`\n"
 
    await message.reply(out_str)


@app.on_message(filters.command("ping"))
async def pingy(client, message):
    start = datetime.now()
    hmm = await message.reply("⚡ Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await hmm.edit(
        f"█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄\n**Ping: {round(ms)}**")



#-------------------------------------------------------------OWNERS SALAMLAMA MSJ---------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

app.start()
print(f"Bot ( {pyrogram.__version__} ilə başladı... Bot'a start verin!")
idle()
