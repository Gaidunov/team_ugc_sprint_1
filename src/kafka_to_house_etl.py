from src.click_house.client import click_client
from src.my_kafka.kafka_consumer import kafka_consumer
from src.utils.logger import get_struct_logger

logger = get_struct_logger(__file__, log_file='src/logs/etl.log')


class Etl:
    def __init__(self) -> None:
        self.kafka_consumer = kafka_consumer
        self.click_house = click_client

    @staticmethod
    def _parse_key(key):
        key = key.decode('utf-8')
        return key.split('+')

    def start_pipeline(self):
        logger.info('ETL process started')
        for key, v in self.kafka_consumer.fetch():
            user_id, movie_id, ts, movie_duration = self._parse_key(key)
            timestamp = v.decode('utf-8')
            self.click_house.add_user_stamp(
                user_id=user_id,
                movie_id=movie_id,
                movie_duration=movie_duration,
                timstamp=timestamp
            )
        logger.info('ETL process ended')


etl = Etl()
etl.start_pipeline()
