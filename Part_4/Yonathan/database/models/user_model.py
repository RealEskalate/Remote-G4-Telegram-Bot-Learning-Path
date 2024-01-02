from pydantic import BaseModel

from ..loader import collection
from datetime import datetime


class User(BaseModel):
    _id: int
    name: str
    date: datetime
    bio: str
    phone_number: str
   


users_collection = collection.user