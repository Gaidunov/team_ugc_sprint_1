from pydantic import BaseModel

class MovieTimeStamp(BaseModel):
    user_id: int
    movie_id: int
    timestamp: int
