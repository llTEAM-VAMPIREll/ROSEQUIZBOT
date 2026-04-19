from aiogram.fsm.state import State, StatesGroup

class QuizCreate(StatesGroup):
    get_title = State()
    get_description = State()
    get_questions = State()
