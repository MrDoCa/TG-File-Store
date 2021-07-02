import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from .commands import start, BATCH
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *

@Client.on_callback_query(filters.regex('^help$'))
async def help_cb(c, m):
    await m.answer()

    # help text
    help_text = """**You need Help?? 🧐**

👉 Send your movies I will save it

__Please try to send good quality movies 😇__

👉 Check it if movie is stored or not by clicking check button

👉 Become a member @IninityCLK and help others by adding new movies 


**⛔️ 𝐍𝐨𝐭𝐞 :**

__📌 Adult content is direct Ban 😡 from bot and from group__

__📌 This bot doesn't save any files in its data base. It stores the file in a hidden/private channel and just forward it to the users who gives the token to it.__


**You can also use me in your channel too 😉**

★ Make me admin in your channel with edit permission. Thats enough now continue uploading files in channel i will edit all posts and add share able link url buttons

**How to enable uploader details in caption**

★ Use /mode command to change and also you can use `/mode channel_id` to control caption for channel msg."""

    # creating buttons
    buttons = [
        [
            InlineKeyboardButton('Home 🏠', callback_data='home'),
            InlineKeyboardButton('About 📕', callback_data='about')
        ],
        [
            InlineKeyboardButton('Close 🔐', callback_data='close')
        ]
    ]

    # editing as help message
    await m.message.edit(
        text=help_text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex('^close$'))
async def close_cb(c, m):
    await m.message.delete()
    await m.message.reply_to_message.delete()


@Client.on_callback_query(filters.regex('^about$'))
async def about_cb(c, m):
    await m.answer()
    owner = await c.get_users(int(OWNER_ID))
    bot = await c.get_me()

    # about text
    about_text = f"""--**📕 My Details:**--

○ ᴍʏ ɴᴀᴍᴇ : [ɪɴғɪɴɪᴛʏ sᴛᴏʀᴇ ʙᴏᴛ](https://t.me/STOREinf_bot)
    
○ ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ

○ ғʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏʀᴏɢʀᴀᴍ

○ ᴠᴇʀsɪᴏɴ : 1.0.0

○ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : 🔐

○ ᴄʀᴇᴀᴛᴏʀ : [ɪɴғɪɴɪᴛʏ ʙᴏᴛs](https://t.me/BOTS_Infinity)

"""

    # creating buttons
    buttons = [
        [
            InlineKeyboardButton('Home 🏠', callback_data='home'),
            InlineKeyboardButton('Help 💡', callback_data='help')
        ],
        [
            InlineKeyboardButton('Close 🔐', callback_data='close')
        ]
    ]

    # editing message
    await m.message.edit(
        text=about_text,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex('^home$'))
async def home_cb(c, m):
    await m.answer()
    await start(c, m, cb=True)


@Client.on_callback_query(filters.regex('^done$'))
async def done_cb(c, m):
    BATCH.remove(m.from_user.id)
    c.cancel_listener(m.from_user.id)
    await m.message.delete()


@Client.on_callback_query(filters.regex('^delete'))
async def delete_cb(c, m):
    await m.answer()
    cmd, msg_id = m.data.split("+")
    chat_id = m.from_user.id if not DB_CHANNEL_ID else int(DB_CHANNEL_ID)
    message = await c.get_messages(chat_id, int(msg_id))
    await message.delete()
    await m.message.edit("Deleted files successfully 👨‍✈️")
