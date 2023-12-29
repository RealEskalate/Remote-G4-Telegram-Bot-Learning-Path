from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    role = State()
    name = State()
    phone_number = State()
    bio = State()
    photo = State()