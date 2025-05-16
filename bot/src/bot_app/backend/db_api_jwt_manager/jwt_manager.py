from src.bot_app.cache.redis_cache import (
    get_jwt_from_cache, save_jwt_to_cache)
from .db_api_jwt_requests import (
    get_jwt_pair_from_db_api, get_access_token_from_db_api)
from src.bot_app.config import Settings


async def get_access_jwt() -> str:
    access_token = await get_jwt_from_cache('access_token')
    if access_token:
        return access_token
    refresh_token = await get_refresh_jwt()
    if refresh_token:
        access_token = await get_access_token_from_db_api(
            Settings.DB_API_URL + 'token/refresh/', refresh_token)
        request_lag_in_seconds = 10
        await save_jwt_to_cache(
            key='access_token',
            ttl=int(Settings.ACCESS_JWT_LIFETIME_IN_MINUTES) * 60 - request_lag_in_seconds,
            value=access_token,
        )

        return access_token

    await get_jwt_pair()
    return await get_jwt_from_cache('access_token')


async def get_refresh_jwt() -> str | None:
    return await get_jwt_from_cache('refresh_token')


async def get_jwt_pair():
    jwt_pair = await get_jwt_pair_from_db_api(
        Settings.DB_API_URL + 'token/',
        Settings.DB_API_USERNAME,
        Settings.DB_API_PASSWORD,
    )
    refresh_token = jwt_pair['refresh']
    access_token = jwt_pair['access']

    request_lag_in_seconds = 10

    await save_jwt_to_cache(
        key='refresh_token',
        ttl=int(Settings.REFRESH_JWT_LIFETIME_IN_DAYS) * 24 * 60 * 60 - request_lag_in_seconds,
        value=refresh_token
    )

    await save_jwt_to_cache(
        key='access_token',
        ttl=int(Settings.ACCESS_JWT_LIFETIME_IN_MINUTES) * 60 - request_lag_in_seconds,
        value=access_token
    )
