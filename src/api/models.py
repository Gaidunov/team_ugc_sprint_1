from pydantic import BaseModel

class MovieTimeStamp(BaseModel):
    user_id: str
    movie_id: str
    timestamp: int
    movie_duration:int

ms = MovieTimeStamp(user_id=1, movie_id=1, title='1', timestamp=1, movie_duration=10)
