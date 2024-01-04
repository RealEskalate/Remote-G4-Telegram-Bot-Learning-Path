from ..loader import collection as users_collection
from bson.objectid import ObjectId

async def get_users():
    users = users_collection.find({})
    return [u for u in users]


async def get_user_by_id(id):
    user = users_collection.find_one({'_id': str(id)})
    return user if user else None


async def create_user(_id, **kwargs):
    user =  users_collection.insert_one({'_id': _id, **kwargs})
    return user

async def delete_user(id):
    user = users_collection.delete_one({'_id': id})
    return 

async def update_user(id, **kwargs):
    user = users_collection.find_one_and_update({'_id': str(id)}, {'$set': kwargs}, return_document=True)
    return user

