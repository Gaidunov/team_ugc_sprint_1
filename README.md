запустить апи для отправки timestamps

```uvicorn src.api.api:app```

отправить тестовые данные 

```python -m src.api.test_views```

прочитать тестовые данные 

```python -m src.kafka.kafka_consumer```

