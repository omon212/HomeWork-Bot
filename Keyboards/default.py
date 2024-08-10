from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Telefon raqamingizni jo'nating 📞", request_contact=True)
        ]
    ],
    resize_keyboard=True
)
