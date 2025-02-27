from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.bot_app.keyboards.inline_keyboards.root_menu_inline_kb import root_menu_kb

router = Router(name=__name__)


@router.message(CommandStart())
async def start_command_handler(message: Message):
    greet_name = (
        message.from_user.username if message.from_user.username
        else message.from_user.first_name
    )
    await message.answer(
        f'Привет, {greet_name}!\nСпасибо, что запустили меня. Я Ноти.\n'
        f'Я помогу с созданием расписаний и напомню о важных делах.',
    )
    await message.answer(
        f'Основное меню {greet_name}',
        reply_markup=root_menu_kb(),
        # one_time_keyboard=True,
    )
