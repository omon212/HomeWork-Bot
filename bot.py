import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from Keyboards.default import *
from Keyboards.inline import *
from config import *
from states import User
from databace import *
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = BOT_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def commands_start(message: types.Message):
    user = await check_user(message.from_user.id)
    if user:
        await message.answer("""
        <b>Tvar uyga vazifani qildingmi ? 🧐</b>
        """, reply_markup=choice_button)
        await User.choice_state.set()
    else:
        await message.answer(f"""<b>
    Assalomu aleykum {message.from_user.full_name}
    
    Avval telefon raqamingiz yuboring ☎️
    </b>""", reply_markup=contact_button)
        await User.contact_state.set()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=User.contact_state)
async def contact_handler(message: types.Message, state: FSMContext):
    await user_data(message.from_user.id, message.from_user.full_name, message.from_user.username,
                    message.contact.phone_number)
    await message.answer("""
<b>Tvar uyga vazifani qildingmi ? 🧐</b>
""", reply_markup=choice_button)
    await state.finish()
    await User.choice_state.set()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
