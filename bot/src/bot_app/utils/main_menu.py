from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_main_menu_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запустить бот.',
        ),
        BotCommand(
            command='help',
            description='Помощь в работе с ботом.',
        ),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
