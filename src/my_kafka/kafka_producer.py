from typing import Any

from kafka import KafkaProducer


class MyKafka(KafkaProducer):

    def __init__(self, **configs):
        super().__init__(**configs)

    def send(self, value: Any, key: Any) -> None:
        print('отправляем ', value)
        super().send(
            topic='user_views',
            value=value,
            key=key,
        )

kafka = MyKafka(bootstrap_servers=['localhost:9092'])
