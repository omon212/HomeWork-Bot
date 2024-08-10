import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove
from collections import defaultdict
from Keyboards.default import *
from Keyboards.inline import *
from config import *
from states import User
from databace import *

BOT_TOKEN = BOT_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

fake_data = defaultdict(dict)


@dp.message_handler(commands=['start'])
async def commands_start(message: types.Message):
    user = await check_user(message.from_user.id)
    print(user)
    if user:
        await message.answer(f"""<b>
Assalomu aleykum {message.from_user.full_name}

Uyga vazifani bajardingizmi 🧐

Siz quyidagi buyruqlardan birini tanlamasangiz ota-onangizni xabar beriladi 🤗
        </b>""", reply_markup=choice_button)
    else:
        await message.answer(f"""<b>
Assalomu aleykum {message.from_user.full_name}

Ro'yxatdan o'tish uchun telefon raqamingizni yuboring 📱
</b>""", reply_markup=contact_button)
        await User.contact_state.set()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=User.contact_state)
async def contact_handler(message: types.Message, state: FSMContext):
    await state.update_data(
        user_id=message.from_user.id,
        fullname=message.from_user.full_name,
        username=message.from_user.username,
        phone_number=message.contact.phone_number
    )
    await message.answer("<b>Guruhingiz raqamini yuboring 🔢</b>", reply_markup=ReplyKeyboardRemove())
    await User.group_state.set()


@dp.message_handler(state=User.group_state)
async def group_handler(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    group_id = int(message.text)
    await user_data_insert(
        user_data['user_id'], user_data['fullname'], user_data['username'],
        user_data['phone_number'], group_id
    )
    await message.answer("<b>Muvaffaqiyatli ro'yxatdan o'tdingiz ✅</b>", reply_markup=ReplyKeyboardRemove())
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
