from aiogram.filters import Command
from aiogram import Router, types
from aiogram.utils.formatting import as_key_value, Bold,as_marked_section, as_list

user_router = Router()

@user_router.message(Command('start'))
async def user_cmd_start(msg: types.message) -> None:
    """Processes start command for users"""
    reply_text = f'Hello, **{msg.from_user.first_name}**'
    await msg.answer(reply_text)

@user_router.message(Command('help'))
async def help_cmd_start(msg: types.message) -> None:
    """Processes help command"""
    content = as_marked_section(
        Bold("Helpful commands"),
        as_key_value("/pending", "To see list of pending orders"),
        as_key_value("/finished", "To see list of finished orders"),
        as_key_value("/delivered", "To see list of delivered orders"),
        marker="➡ "
    )
    await msg.answer(**content.as_kwargs())

@user_router.message(Command('finished','delivered', 'pending'))
async def other_cmd(msg: types.message) -> None:
    reply_text = "this command is not yet implemented"
    await msg.answer(reply_text)