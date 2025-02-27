from aiogram import F, Router
from aiogram.types import Message

from src.bot_app.backend.db_api_requests import get_db_api_jwt_tokens_from_backend
from src.bot_app.config import Settings

router = Router(name=__name__)


@router.message(F.text == '/api')
async def message(message: Message):
    await get_db_api_jwt_tokens_from_backend(
        Settings.DB_API_ADDRESS + 'token/',
        Settings.DB_API_USERNAME,
        Settings.DB_API_PASSWORD,
    )
    await message.answer("api_sent")
