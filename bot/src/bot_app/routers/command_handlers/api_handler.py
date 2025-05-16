from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


from src.bot_app.backend.db_api_jwt_manager.db_api_jwt_requests import get_jwt_pair_from_db_api
from src.bot_app.config import Settings

router = Router(name=__name__)


@router.message(Command('api', prefix='!/'))
async def api_message(message: Message):
    jwt_data = await get_jwt_pair_from_db_api(
        Settings.DB_API_URL + 'token/',
        Settings.DB_API_USERNAME,
        Settings.DB_API_PASSWORD,
    )
    print(jwt_data)
    print(jwt_data['access'])
    print(jwt_data['refresh'])

    payload = jwt_data['access']

    await message.answer("api_sent")
