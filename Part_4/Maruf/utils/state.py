from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    name = State()
    _id = State()
    age = State()
    delete_id = State()
    update_id = State()
    update_name = State()
    update_age = State()
    update_both = State()

