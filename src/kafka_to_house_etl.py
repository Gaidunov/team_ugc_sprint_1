from src.click_house.client import click_client
from src.my_kafka.kafka_consumer import kafka_consumer


class Etl:
    
    def __init__(self) -> None:
        self.kafka_consumer = kafka_consumer
        self.click_house = click_client

    @staticmethod
    def _parse_key(key):
        key = key.decode('utf-8')
        return key.split('+')

    def start_pipeline(self):
        for key, v in self.kafka_consumer.fetch():

            user_id, movie_id = self._parse_key(key)
            timestemp = v.decode('utf-8')
            self.click_house.add_user_stamp(user_id, movie_id, timestemp)

etl = Etl()
etl.start_pipeline()
