import random
import json
import asyncio

import aiohttp

from src.api.models import MovieTimeStamp
from src.utils.logger import get_struct_logger

logger = get_struct_logger(__name__, log_file='src/logs/etl.log')


async def test_api_kafka():
    '''симулируем просмотр фильмов множеством юзеров'''

    with open('src/api/movies_with_time.json', 'r', encoding='utf-8') as f:
        movies = json.load(f)
    
    users = [e for e in range(100)]
    async with aiohttp.ClientSession() as session:
        for _ in range(100):  # загружаем тестовых 100 меток
            movie_id, _, movie_duration = random.choice(movies)
            timestamp = random.randint(0, movie_duration)
            user_id = random.choice(users)
            request_body = MovieTimeStamp(user_id=user_id,
                                          movie_id=movie_id,
                                          timestamp=timestamp,
                                          movie_duration=movie_duration)
            async with session.post('http://127.0.0.1:8000/send_stamp', json=request_body.dict()) as resp:
                if resp.status == 200:
                    logger.info('timestamp sent')
                
asyncio.run(test_api_kafka())
