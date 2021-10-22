from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from config import  ASSISTANT_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, BOT_USERNAME
from plugins.tr import *
from pyrogram.errors import MessageNotModified

@Client.on_message(filters.command("start"))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="help"),
            ],
            [
                InlineKeyboardButton("🌿🎶", url=f"https://{SUPPORT_GROUP}"),
                InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("Dᴇᴠꜱ", callback_data="devs"),
            ],
            [
               InlineKeyboardButton("Sᴜᴍᴍᴏɴ Mᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   if message.chat.type == 'private':
       await message.reply_text(
          START_TEXT,
          reply_markup=reply_markup
       )
   else:
      await message.reply(f"**@{ASSISTANT_NAME} Çalışıyor! ✨**")

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start"),
                InlineKeyboardButton ("Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="about":
        buttons = [
            [
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start"),
                InlineKeyboardButton ("Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ABOUT_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="devs":
        buttons = [
            [
                InlineKeyboardButton("Sahip", url="https://t.me/Ruhsuzbeyyy"),
                InlineKeyboardButton("Eʀʀᴏʀ", url="https://t.me/Ruhsuzbeyyy"),
            ],
            [
                InlineKeyboardButton("SUPPORT_GROUP", url="https://t.me/Alem_Sohbet"),
                InlineKeyboardButton("SUPPORT_GROUP", url="https://t.me/Universite_Sohbet"),
            ],
            [
                InlineKeyboardButton("kanal", url="https://t.me/korsanfed"),
                InlineKeyboardButton("desdek", url="https://t.me/cakiltasim"),
            ],
            [
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                DEVS_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="start":
        buttons = [
            [
                InlineKeyboardButton("Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="help"),
            ],
            [
                InlineKeyboardButton("SUPPORT_GROUP", url=f"https://{SUPPORT_GROUP}"),
                InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("Dᴇᴠꜱ", callback_data="devs"),
            ],
            [
               InlineKeyboardButton("beni kullan", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
