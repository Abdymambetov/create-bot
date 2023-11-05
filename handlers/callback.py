from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot

# @dp.callback_query_handler(text='button_call_1')
async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('NEXT', callback_data='button_call_2')
    markup.add(button_call_2)
    question = "Who is Lewis Hamilton?"
    answers = [
        "Recer",
        "Dancer",
        "Boxer",
        "Driver"
    ]
    await bot.send_poll(
        call.from_user.id, 
        question, 
        options=answers, 
        is_anonymous=True, 
        type='quiz', 
        correct_option_id=0,
        explanation='You are stupid',
        open_period=10,
        reply_markup=markup
    )

# @dp.callback_query_handler(text='button_call_2')
async def quiz3(call: types.CallbackQuery):
    question = "Who is the best racer in the world?"
    answers = [
        "Lewis Hamilton",
        "Shumaher",
        "Ricardo",
        "Max Verstapen"
    ]
    photo = open('./assets/photo_2023-03-30 14.15.28.jpeg', 'rb')
    await bot.send_photo(call.from_user.id, photo)

    await bot.send_poll(
        call.from_user.id, 
        question, 
        options=answers, 
        is_anonymous=True, 
        type='quiz', 
        correct_option_id=0,
        explanation='You are stupid',
        open_period=10,
    )

def register_hendlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2, text='button_call_1')
    dp.register_callback_query_handler(quiz3, text='button_call_2')
    