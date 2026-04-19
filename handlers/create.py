import asyncio
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from states import QuizCreate

def register(dp):

    @dp.callback_query(F.data == "create_quiz")
    async def create_start(call: types.CallbackQuery, state: FSMContext):
        await call.message.answer("⏳ Quiz creator open ho raha hai...")
        await asyncio.sleep(1)
        await call.message.answer("📘 Quiz title bhejo:")
        await state.set_state(QuizCreate.get_title)

    @dp.message(QuizCreate.get_title)
    async def title(message: types.Message, state: FSMContext):
        await state.update_data(title=message.text)
        await message.answer("📝 Description bhejo ya /skip likho")
        await state.set_state(QuizCreate.get_description)

    @dp.message(QuizCreate.get_description)
    async def desc(message: types.Message, state: FSMContext):
        desc = "No description" if message.text == "/skip" else message.text
        await state.update_data(desc=desc)

        kb = InlineKeyboardBuilder()
        kb.button(text="➕ Question Add karo", callback_data="add_q")

        await message.answer("👉 Question add karna start karo", reply_markup=kb.as_markup())

    @dp.callback_query(F.data == "add_q")
    async def add_q(call: types.CallbackQuery, state: FSMContext):
        await call.message.answer("📊 Poll open karo (Quiz mode ON)")
        await state.set_state(QuizCreate.get_questions)

    @dp.message(F.poll, QuizCreate.get_questions)
    async def save_poll(message: types.Message):
        if message.poll.is_anonymous:
            await message.answer("❌ Anonymous OFF karo")
            return

        await message.answer("✅ Question save ho gaya!")
