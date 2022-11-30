from typing import Any

from kafka import KafkaProducer


class Kafka:
    # TODO: порты в env
    def __init__(self) -> None:
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def send(self, value: Any, key: Any) -> None:
        self.producer.send(
            topic='views',
            value=value,
            key=key,
        )

kafka = Kafka()
