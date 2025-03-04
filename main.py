import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('TG_TOKEN'))
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    msg = os.getenv('MESSAGE')
    await message.answer(f'Hello, world from bot. {msg}!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

