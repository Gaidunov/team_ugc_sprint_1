0. Поднять докер
``` Make go ```

1. запустить апи для отправки timestamps

```uvicorn src.api.api:app```

2. начать принимать сообщения из кафки и загружать в кликхаус

```python3 -m src.kafka_to_house_etl```

3. отправить тестовые данные 

```python3 -m src.api.fake_views```


