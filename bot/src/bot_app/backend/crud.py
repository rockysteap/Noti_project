from src.bot_app.backend.db_api_jwt_manager.db_api_requests import request_api_w_access_token
from src.bot_app.backend.models import NotiOwner
from src.bot_app.backend.db_api_jwt_manager import jwt_manager
from src.bot_app.config import Settings

"""
NotiOwner -------------------------------------------
"""


async def read_or_create(telegram_id: int):
    access_token = await jwt_manager.get_access_jwt()
    data = await request_api_w_access_token(
        api_url=Settings.DB_API_URL + 'noti_owner/',
        access_token=access_token,
        telegram_id=telegram_id,
    )
    return data


async def update():
    ...


async def delete(key) -> None:
    ...
