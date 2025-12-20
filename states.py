from aiogram.fsm.state import StatesGroup, State

class RegisterState(StatesGroup):
    WAITING_FOR_NAME = State()
    WAITING_FOR_PHONE_NUMBER = State()

class PostCommandState(StatesGroup):
    WAITING_FOR_POST_CONTENT = State()

class ScheduleState(StatesGroup):
    WAITING_FOR_SCHEDULE_POST = State()
    WAITING_FOR_SCHEDULE_TIME = State()

    WAITING_CHECK = State()

class ConsultationState(StatesGroup):
    waiting_for_age = State()
    waiting_for_education_or_work = State()
    waiting_for_question1 = State()
    waiting_for_question2 = State()
    waiting_for_question3 = State()
    waiting_for_question4 = State()
