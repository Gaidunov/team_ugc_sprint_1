from typing import Any

from kafka import KafkaProducer

from src.config import config
from src.utils.logger import get_struct_logger

logger = get_struct_logger(__file__, log_file='src/logs/etl.log')


class MyKafka(KafkaProducer):

    def __init__(self, **configs):
        super().__init__(**configs)

    def send(self, value: Any, key: Any) -> None:
        
        logger.info('Kafka sends {value}')
        super().send(
            topic=config.kafka_topic,
            value=value,
            key=key,
        )


kafka = MyKafka(bootstrap_servers=[f'{config.kafka_host}:{config.kafka_port}'])
