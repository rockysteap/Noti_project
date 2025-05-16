from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name=__name__)


@router.message(Command('help', prefix='!/'))
async def help_command(message: Message):
    await message.answer('Помощь всё ещё в пути')
