from pydantic import BaseModel

# from ..loader import collection
from datetime import datetime


class User(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    occupation: str
    phone_number: int
    photo_id: str

   

# users_collection = collection.user