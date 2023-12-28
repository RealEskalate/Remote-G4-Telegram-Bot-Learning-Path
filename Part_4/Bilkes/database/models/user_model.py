from pydantic import BaseModel

from ..loader import collection
from datetime import datetime


class User(BaseModel):
    _id: int
    name: str
    age:int
    phone_number: str
    photo_id: str
    date: datetime
   


users_collection = collection.user