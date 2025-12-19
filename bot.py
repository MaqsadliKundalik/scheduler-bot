from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from models import init_db
from message import admin, user, tasks
from asyncio import create_task, run
from logging  import basicConfig, INFO
from aiogram.client.default import DefaultBotProperties
from middlewares import CheckSUbChannelMiddleware

basicConfig(level=INFO)

dp = Dispatcher()
dp.include_router(admin.router)
dp.include_router(user.router)
dp.message.middleware(CheckSUbChannelMiddleware())

async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(protect_content=True))
    await init_db()
    create_task(tasks.send_posts_task(bot))
    await dp.start_polling(bot)

if __name__ == "__main__":
    run(main())