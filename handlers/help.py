from aiogram import types, F

def register(dp):

    @dp.callback_query(F.data == "help_menu")
    async def help_menu(call: types.CallbackQuery):
        await call.message.answer(
            "📚 Commands:\n\n/start - Bot start\n/create - Quiz create"
        )
