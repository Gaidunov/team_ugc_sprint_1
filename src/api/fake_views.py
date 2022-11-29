import random
import json
import asyncio

import aiohttp

from src.api.models import MovieTimeStamp

with open('src/api/movies_with_time.json', 'r', encoding='utf-8') as f:
    movies = json.load(f)

users = [e for e in range(1000)]


async def test_api_kafka():
    '''симулируем просмотр фильмов множеством юзеров'''
    
    async with aiohttp.ClientSession() as session:
        for _ in range(100): # загружаем 100 меток 
            movie_id, _, timestamp = random.choice(movies)
            user_id = random.choice(users)
            request_body = MovieTimeStamp(user_id=user_id,
                                          movie_id=movie_id,
                                          timestamp=timestamp)
            async with session.post('http://127.0.0.1:8000/send_stamp', json=request_body.dict()) as resp:
                print(resp.status)
            
asyncio.run(test_api_kafka())

