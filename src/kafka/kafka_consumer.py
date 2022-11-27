from kafka import KafkaConsumer


consumer = KafkaConsumer(
    'views',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='echo-messages-to-stdout',
)

for message in consumer:
    print('user+movie', message.key, 'timestamp' ,message.value)
