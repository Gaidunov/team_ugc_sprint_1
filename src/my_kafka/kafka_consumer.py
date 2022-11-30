from kafka import KafkaConsumer

class Consumer:

    def fetch(self):
        consumer = KafkaConsumer(
            'views',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            group_id='echo-messages-to-stdout',
        )

        for message in consumer:
            yield message.key, message.value

kafka_consumer = Consumer()
