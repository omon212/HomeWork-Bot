from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha ✅", callback_data="yes"),
            InlineKeyboardButton(text="Yo'q ❌", callback_data="no")
        ]
    ]
)
