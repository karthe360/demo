# models.py

from typing import List

class Room:
    def __init__(self, id: int, type: str, price: float, available: bool):
        self.id = id
        self.type = type
        self.price = price
        self.available = available
