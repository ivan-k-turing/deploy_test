from pydantic import BaseModel


class HouseInfo(BaseModel):
    square_meters: float
    floors: int
    sleeping_rooms: int
    bathrooms: int


class Prediction(BaseModel):
    price: float
