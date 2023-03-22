from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton #düyməsi yoxdur.!
import pyrogram
from Config import Config
from datetime import datetime
from telethon import Button


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


#-------------------------------------------------------------OWNERS SALAMLAMA MSJ---------------------------------------------------------------------------------------#
        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply('[𝗦Σ𝗠Δ 𝗧Δ𝗚𝗚Σ𝗥](https://t.me/Sematagbot)-un Sahibi, Qrupa Qatıldı.\n Xoş Gəldin  Aramıza Sahib, Necəsən?🥰.')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

app.start()
print(f"Bot ( {pyrogram.__version__} ilə başladı... Bot'a start verin!")
idle()
