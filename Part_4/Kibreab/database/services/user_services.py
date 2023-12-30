from ..models.user_model import User, users_collection, UsersResponse


async def get_users() -> UsersResponse:
    users = await users_collection.find().to_list(length=None)
    return UsersResponse(users=[User(**u) for u in users])


async def get_user_by_id(id: int) -> User or None:
    user = await users_collection.find_one({'_id': id})
    return User(**user) if user else None


async def create_user(id: int, **kwargs) -> User:
    user = await users_collection.insert_one({'_id': id, **kwargs})
    return await get_user_by_id(user.inserted_id)


async def update_user(id: int, **kwargs) -> User:
    user = await users_collection.find_one_and_update({'_id': id}, {'$set': kwargs}, return_document=True)
    return User(**user)
