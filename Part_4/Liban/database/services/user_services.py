from ..models.user_model import User
from ..loader import get_all_users, get_user_by_id, register_user, update_user_by_id, delete_user_by_id, filter_users_by_name



async def get_users() -> list[User]:
    users = get_all_users()
    return [User(**u) async for u in users]


def get_user_by_id(id: int) -> User or None:
    user = get_user_by_id(id)
    return User(**user) if user else None


def create_user(**kwargs) -> User:
    print(kwargs)
    user = register_user(**kwargs)
    return user


def update_user(id: int, **kwargs) -> User:
    user = update_user_by_id({'_id': id}, {'$set': kwargs}, return_document=True)
    return User(**user)


async def delete_user(id: int) -> bool:
    result = delete_user_by_id({'_id': id})
    return result.deleted_count > 0


async def filter_users_by_name(name: str) -> list[User]:
    users =filter_users_by_name({'name': name})
    return [User(**u) async for u in users]
