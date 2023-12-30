from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    country = State()
    name = State()
    phone_number = State()
    photo = State()
    bio = State()