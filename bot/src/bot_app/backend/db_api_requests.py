import aiohttp


async def get_db_api_jwt_tokens_from_backend(db_api_url, db_api_username, db_api_password):
    payload = {
        'username': db_api_username,
        'password': db_api_password,
    }
    headers = {
        'Content-Type': 'application/json',
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url=db_api_url, json=payload, headers=headers) as response:
            if response.status != 200:
                print(Exception(f'API request failed with status {response.status}'))
            data = await response.json()
            refresh_token = data.get('refresh')
            access_token = data.get('access')

            with open('../.db_api_jwt_refresh_token', 'w') as jwt_file:
                jwt_file.write(f'{refresh_token}')
            with open('../.db_api_jwt_access_token', 'w') as jwt_file:
                jwt_file.write(f'{access_token}')
