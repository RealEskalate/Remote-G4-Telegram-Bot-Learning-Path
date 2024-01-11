from datetime import datetime
from typing import List, Union

from ..models.user_model import User, users_collection

async def get_users() -> str:
    users = [user async for user in users_collection.find()]

    if not users:
        return "No registered users yet."

    response = (
        "<b>Registered Users:</b>\n\n"
        "<pre>ID           | Name          | Date\n"
        "------------------------------------------\n"
        + "\n".join(
            f"{str(user['_id']):<13} | {user['name'][:14]:<14} | {str(user['date'].strftime('%Y-%m-%d'))[:20]}"
            for user in users
        )
        + "</pre>"
    )

    return response

async def get_user_by_id(id: int) -> Union[User, None]:
    user = await users_collection.find_one({"_id": id})
    return User(**user) if user else None

async def create_user(id: int, **kwargs) -> Union[User, None]:
    user = await users_collection.insert_one({"_id": id, **kwargs})
    return await get_user_by_id(user.inserted_id)

async def update_user(id: int, **kwargs) -> Union[User, str]:
    result = await users_collection.update_one({"_id": id}, {"$set": kwargs})

    if result.matched_count == 0:
        return "You haven't registered yet!"

    if result.modified_count > 0:
        updated_user = await users_collection.find_one({"_id": id})
        return User(**updated_user)

    return "No modifications were made."
