from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")  # Получаем токен из переменных среды

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="ABZ",
                    web_app=WebAppInfo(url="https://tg.app.abz.gl/index.html#/home")
                )
            ]
        ]
    )
    await message.answer("Нажми на кнопку, чтобы открыть Web App:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
