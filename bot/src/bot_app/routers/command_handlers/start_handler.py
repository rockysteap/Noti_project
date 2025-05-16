from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.bot_app.keyboards.inline_keyboards.root_menu_inline_kb import root_menu_kb
from src.bot_app.backend.controller import init_user

router = Router(name=__name__)


# /start
@router.message(CommandStart())
async def start_command_handler(message: Message):

    # controller ->

    # controller -> init_user
    await init_user(message.from_user.id)

    greet_name = (
        message.from_user.full_name if message.from_user.full_name
        else message.from_user.first_name
    )
    await message.answer(
        f'Привет, {greet_name}!\nСпасибо, что запустили меня. Я Ноти.\n'
        f'Я помогу с созданием расписаний и напомню о важных делах.',
    )
    await message.answer(
        'Основное меню',
        reply_markup=root_menu_kb(),
    )
