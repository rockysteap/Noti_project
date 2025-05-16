import aiohttp


async def request_api_w_access_token(api_url, access_token, *args, **kwargs):
    payload = {
        **kwargs,
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}',
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, json=payload, headers=headers) as response:
            if response.status not in (200, 201):
                print(Exception(
                    f'{request_api_w_access_token.__name__}: API request failed with status {response.status}'))
            data = await response.json()

            return data
