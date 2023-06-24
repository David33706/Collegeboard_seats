from aiogram import types
from data.config import ADMINS
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main_btn import ctry_markup
from states.main_state import countryname
from loader import dp,db, bot
import sqlite3


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    await message.answer(
        "This is collegeboard bot.\nIts main purpose to help you check if seats for the chosen date are avialable\nPlease choose preferable country and test date",
        reply_markup=ctry_markup)
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} added to the base.\n {count} users in the bot."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
    await countryname.country.set()

