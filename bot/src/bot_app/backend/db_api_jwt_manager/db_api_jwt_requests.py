import aiohttp


async def get_jwt_pair_from_db_api(db_api_url, db_api_username, db_api_password):
    payload = {
        'username': db_api_username,
        'password': db_api_password,
    }
    headers = {
        'Content-Type': 'application/json',
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url=db_api_url, json=payload) as response:
            if response.status != 200:
                print(Exception(f'{get_jwt_pair_from_db_api.__name__}: API request failed with status {response.status}'))

            data = await response.json()
            refresh_token = data.get('refresh')
            access_token = data.get('access')

            with open('../.db_api_jwt_refresh_token', 'w') as jwt_file:
                jwt_file.write(f'{refresh_token}')
            with open('../.db_api_jwt_access_token', 'w') as jwt_file:
                jwt_file.write(f'{access_token}')

            return await response.json()


async def get_access_token_from_db_api(db_api_url, refresh_jwt):
    payload = {
        'refresh': refresh_jwt,
    }
    headers = {
        'Content-Type': 'application/json',
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url=db_api_url, json=payload) as response:
            if response.status != 200:
                print(Exception(f'{get_access_token_from_db_api.__name__}: API request failed with status {response.status}'))

            data = await response.json()
            access_token = data.get('access')

            with open('../.db_api_jwt_access_token', 'w') as jwt_file:
                jwt_file.write(f'{access_token}')

            return data.get('access')

            # data = await response.json()
            # refresh_token = data.get('refresh')
            # print(f'refresh_token: {refresh_token}')
