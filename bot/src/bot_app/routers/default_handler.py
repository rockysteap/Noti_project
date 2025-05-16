from aiogram import Router, F
from aiogram.types import Message

router = Router(name=__name__)


@router.message()
async def default_handler(message: Message):
    await message.reply('Сообщение получено, но обработано не было.')