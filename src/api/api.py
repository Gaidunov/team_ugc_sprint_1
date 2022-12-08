from fastapi import FastAPI
from http import HTTPStatus

from src.api.models import MovieTimeStamp
from src.my_kafka.kafka_producer import kafka
from src.auth import token_verification

 
app = FastAPI(docs_url='/docs')


@app.post("/send_stamp")
@token_verification
async def send_time_stamp(data:MovieTimeStamp):
    """отправляем в кафку инфу о прогрессе просмотра фильма юзером"""
    # user_id, movie_id, ts, movie_duration
    encoded = list(map(lambda x: str(x).encode('utf-8'), list(data.dict().values())))
    key = '+'.encode('utf-8').join(encoded)
    value = str(data.timestamp).encode('utf-8')
    kafka.send(key=key, value=value)
    return HTTPStatus.OK
    