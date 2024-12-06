# main.py

from fastapi import FastAPI, HTTPException
from typing import List
from models import Room
from schemas import RoomCreate, Room as RoomResponse

app = FastAPI()

# In-memory database (a simple list to store rooms)
fake_db = []

# Create a room
@app.post("/rooms/", response_model=RoomResponse)
async def create_room(room: RoomCreate):
    room_id = len(fake_db) + 1
    new_room = Room(id=room_id, **room.dict())
    fake_db.append(new_room)
    return new_room

# Get all rooms
@app.get("/rooms/", response_model=List[RoomResponse])
async def get_rooms():
    return fake_db

# Get room by ID
@app.get("/rooms/{room_id}", response_model=RoomResponse)
async def get_room(room_id: int):
    room = next((r for r in fake_db if r.id == room_id), None)
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return room
