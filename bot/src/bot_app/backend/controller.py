from src.bot_app.backend.models import NotiOwner
from src.bot_app.cache.redis_cache import get_value_from_cache
from src.bot_app.backend import crud


async def init_user(telegram_id: int):
    data = await get_value_from_cache(telegram_id)
    if not data:
        data = await get_or_create_user_in_db(telegram_id)

    # user = NotiOwner(id=data['id'], telegram_id=data['telegram_id'])
    print(data)
    user = NotiOwner(**data)
    json_data = user.model_dump_json()
    model_data = NotiOwner.model_validate_json(json_data)
    model_data2 = NotiOwner.model_validate_json(json_data)
    print(model_data.id == model_data2.id)
    print(model_data)
    print(model_data2)

    # print(f'{init_user.__name__}: {model_data=}, {type(model_data)=}')
    #   init_user: model_data=NotiOwner(id=1, telegram_id='6002292650'),
    #   type(model_data)=<class 'src.bot_app.backend.models.NotiOwner'>


async def get_or_create_user_in_db(telegram_id: int):
    return await crud.read_or_create(telegram_id)
