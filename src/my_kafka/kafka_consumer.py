from kafka import KafkaConsumer
from src.config import config


class Consumer:
    def fetch(self):
        consumer = KafkaConsumer(
            config.kafka_topic, 
            bootstrap_servers=config.kafka_bootstrap_servers,
            auto_offset_reset='earliest',
            group_id='echo-messages-to-stdout',
        )

        for message in consumer:
            yield message.key, message.value


kafka_consumer = Consumer()
