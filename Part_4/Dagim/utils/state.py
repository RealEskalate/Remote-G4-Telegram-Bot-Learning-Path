from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    user_id = State()
    first_name = State()
    last_name = State()
    phone_number = State()
    photo = State()
    bio = State()
    
class Unauth(StatesGroup):
    user_id = State()