from pydantic import BaseModel
from typing import List

from ..loader import collection
from datetime import datetime


class User(BaseModel):
    _id: int
    name: str
    phone_number: str
    role: str
    photo_id: str
    date: datetime

class UsersResponse(BaseModel):
    users: List[User]
   

users_collection = collection.user