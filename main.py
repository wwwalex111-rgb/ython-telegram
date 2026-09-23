import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Получа ток из переменных окружения (безопасный метод&)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.reply(
        "👋 Hello! This is a demo bot running on a test Python server.\n"
        "It is used for backend performance testing and API benchmarking."
    )

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"Echo response: {message.text}")

async def main():
    print("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
