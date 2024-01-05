from ..models.user_model import User, users_collection


async def get_users() -> list:
    users = [user async for user in users_collection.find()]

    if users:
        response = "<b>Registered Users:</b>\n\n"
        response += "<pre>"
        response += "ID           | Name          | Date\n"
        response += "------------------------------------------\n"

        for user in users:
            user_info = (
                str(user["_id"]),
                user["name"],
                str(user["date"].strftime("%Y-%m-%d")),
            )
            response += (
                f"{user_info[0]:<13} | {user_info[1][:14]:<14} | {user_info[2][:20]}\n"
            )

        response += "</pre>"

        return response
    else:
        return "No registered users yet."


async def get_user_by_id(id: int) -> User or None:
    user = await users_collection.find_one({"_id": id})
    return user if user else None


async def create_user(id: int, **kwargs) -> User or None:
    user = await users_collection.insert_one({"_id": id, **kwargs})
    return await get_user_by_id(user.inserted_id)


async def update_user(id: int, **kwargs) -> User or None:
    result = await users_collection.update_one({"_id": id}, {"$set": kwargs})

    if result.matched_count == 0:
        return "You haven't registered yet!"

    if result.modified_count > 0:
        updated_user = await users_collection.find_one({"_id": id})
        return User(**updated_user)

    return "No modifications were made."
