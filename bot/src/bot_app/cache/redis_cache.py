"""
cached items:
-------------
access_token: <access jwt>
refresh_token: <refresh jwt>

"""
import functools

import redis
from aiogram.fsm.storage.redis import RedisStorage

from src.bot_app.config import Settings

redis_password = Settings.REDIS_PASSWORD

pool = redis.asyncio.ConnectionPool(
    host='localhost',
    port=6379,
    db=0,
    password=redis_password,
    max_connections=10,
)

r = redis.asyncio.StrictRedis(connection_pool=pool, decode_responses=True)

cache_storage = RedisStorage(redis=r)


def handle_redis_exceptions(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            print('REDIS ERROR: ', e)
            return None

    return wrapper


@handle_redis_exceptions
async def save_jwt_to_cache(key, ttl, value):
    # ttl - time to live in seconds
    await r.setex(key, ttl, value)


@handle_redis_exceptions
async def get_jwt_from_cache(key):
    data = await r.get(key)
    if data:
        return data.decode('utf-8')
    return None


@handle_redis_exceptions
async def save_key_value_to_cache(key, value):
    await r.set(key, value)


@handle_redis_exceptions
async def get_value_from_cache(key):
    data = await r.get(key)
    if data:
        return data.decode('utf-8')
    return None
