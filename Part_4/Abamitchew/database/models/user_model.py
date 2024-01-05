from pydantic import BaseModel

from ..loader import collection
from datetime import datetime


class User(BaseModel):
    _id: int
    name: str
    phone_number: str
    role: str
    a2sv_no: str
    date: datetime
   


users_collection = collection.user