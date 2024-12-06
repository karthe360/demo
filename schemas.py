# schemas.py

from pydantic import BaseModel

class RoomBase(BaseModel):
    type: str
    price: float
    available: bool

class RoomCreate(RoomBase):
    pass

class Room(RoomBase):
    id: int

    class Config:
        orm_mode = True
