import random
import asyncio
import json 

import aiohttp

from src.api.models import MovieTimeStamp


async def test_api_kafka():
    '''симулируем просмотр фильмов множеством юзеров'''

    async with aiohttp.ClientSession() as session:
        for _ in range(10):
            request_body = MovieTimeStamp(
                    movie_id=random.randint(1, 1000),
                    user_id=random.randint(1, 1000),
                    timestamp=random.randint(1, 14400)
                )
            async with session.post('http://127.0.0.1:8000/send_stamp', json=request_body.dict()) as resp:
                print(resp.status)
        

asyncio.run(test_api_kafka())

