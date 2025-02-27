from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from .config import Settings

from .routers import router as main_router

from src.bot_app.utils.main_menu import set_main_menu_commands
from src.bot_app.cache.redis_cache import cache_storage


async def bot_main():
    bot = Bot(token=Settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=cache_storage)
    dp.include_router(main_router)

    try:
        await set_main_menu_commands(bot)
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()
