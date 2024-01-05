from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    name = State()
    phone_number = State()
    role = State()
    photo = State()
    a2sv_batch_no=State()