import uuid
import random

from clickhouse_driver import Client
from src.utils.logger import get_struct_logger
from src.config import config


logger = get_struct_logger(__file__, log_file='src/logs/etl.log')


class ClickHouseClient:

    def __init__(self) -> None:
        self.client = Client(host='localhost')  
        self.logger = logger.bind(topic=config.kafka_topic)

    def add_user_stamp(self, user_id:str, movie_id:str, movie_duration:int, timstamp:int):
        """добавялем юзерские метки"""
        self.client.execute(f"""INSERT INTO 
                                default.users_views (id, user_id, movie_id, movie_duration, timestamp) 
                                VALUES 
                                (generateUUIDv4(), '{user_id}', '{movie_id}', '{movie_duration}', {timstamp})""")
        
        self.logger.info(event=f'сохранили в кликхаус', data=f'{user_id} {movie_id} {movie_duration} {timstamp}')


    def add_test_timestamps(self):
        """тестим insert into кликхаус"""
        for e in range(1,100):
            self.add_user_stamp(user_id=f'{uuid.uuid4()}', movie_id=f'movie_uid_{e}', movie_duration=random.randint(6000,12000), timstamp=random.randint(1, 12000))

    def test_get(self):
        """тестим get from кликхаус"""
        return self.client.execute("select * from default.users_views where user_id='42' ")

    
click_client = ClickHouseClient()
