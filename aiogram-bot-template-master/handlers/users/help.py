from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(
        "This is collegeboard bot.\nIts main purpose to help you check if seats for the chosen date are avialable\nPlease choose preferable country and test date",)
