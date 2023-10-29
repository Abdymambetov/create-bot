from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
import logging

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def starthandler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Greatings, {message.from_user.first_name}!")
    await message.answer("This is an answer method!")
    await message.reply("This is an reply method")

@dp.message_handler(commands=['quiz'])
async def sendQuiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup.add(button_call_1, )
    question = "How many times Lewis Hamilton won the Formula 1 World Championship?"
    answers = [
        "7",
        "8",
        "6",
        "4"
    ]
    await bot.send_poll(
        message.from_user.id, 
        question, 
        options=answers, 
        is_anonymous=True, 
        type='quiz', 
        correct_option_id=0,
        explanation='You are stupid',
        open_period=10,
        reply_markup=markup
    )

@dp.callback_query_handler(text='button_call_1')
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

@dp.callback_query_handler(text='button_call_2')
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
    
@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    await bot.send_message(message.from_user.id, message.text)


if __name__ == "__name__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
