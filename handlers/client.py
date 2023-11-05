from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot
from keyboards.klient_kb import start_markup


# @dp.message_handler(commands=['start', 'help'])
async def starthandler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Greatings, {message.from_user.first_name}!", reply_markup=start_markup)

    # await message.answer("This is an answer method!")
    # await message.reply("This is an reply method")

# @dp.message_handler(commands=['quiz'])
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

async def info_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"сам разебершься {message}")

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(starthandler, commands=['start', 'help'])
    dp.register_message_handler(sendQuiz1, commands=['quiz'])
    dp.register_message_handler(info_handler, commands=['info'])