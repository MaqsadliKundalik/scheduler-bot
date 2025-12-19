from aiogram.fsm.state import StatesGroup, State

class RegisterState(StatesGroup):
    WAITING_FOR_NAME = State()
    WAITING_FOR_PHONE_NUMBER = State()

class PostCommandState(StatesGroup):
    WAITING_FOR_POST_CONTENT = State()

class ScheduleState(StatesGroup):
    WAITING_FOR_SCHEDULE_POST = State()
    WAITING_FOR_SCHEDULE_TIME = State()

