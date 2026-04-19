from aiogram import types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import OWNER_ID, SUPPORT_CHANNEL, WELCOME_IMAGE

def register(dp):

    @dp.message(Command("start"))
    async def start_cmd(message: types.Message):

        kb = InlineKeyboardBuilder()

        kb.row(types.InlineKeyboardButton(
            text="➕ Add Bot in Group",
            url=f"https://t.me/{(await message.bot.get_me()).username}?startgroup=true"
        ))

        kb.row(types.InlineKeyboardButton(
            text="📊 Create Quiz",
            callback_data="create_quiz"
        ))

        kb.row(
            types.InlineKeyboardButton(
                text="Owner",
                url=f"tg://user?id={OWNER_ID}"
            ),
            types.InlineKeyboardButton(
                text="Help",
                callback_data="help_menu"
            )
        )

        kb.row(types.InlineKeyboardButton(
            text="Support Channel",
            url=SUPPORT_CHANNEL
        ))

        await message.answer_photo(
            photo=WELCOME_IMAGE,
            caption="🔥 PREMIUM QUIZ BOT READY\n\nGroup + DM Quiz System\nFast & Simple Quiz Creator",
            reply_markup=kb.as_markup(),
            parse_mode="Markdown"
        )
