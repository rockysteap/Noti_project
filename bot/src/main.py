import asyncio

from src.bot_app.app import bot_main

if __name__ == '__main__':
    try:
        asyncio.run(bot_main())
    except KeyboardInterrupt:
        print("Бот остановлен")
