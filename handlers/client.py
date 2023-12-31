from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot
from keyboards.klient_kb import start_markup
from handlers.fsm_anketa import fsm_start
from database.bot_db import sql_command_random
from handlers.admin import delete_data
from parser import cartoons

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


async def dice_game(message: types.Message):
    print(message)
    user = 0
    comp = 0
    num_user = await bot.send_dice(message.chat.id, emoji='🎲')
    num_comp = await bot.send_dice(message.chat.id, emoji='🎲')
    print(num_user.dice.value, 'user')
    print(num_comp.dice.value, 'comp')
    user = num_user.dice.value
    comp = num_comp.dice.value
    if user > comp:
        await bot.send_message(message.from_user.id, f"Ты победил ты: {user}, комьютер: {comp}")
    elif user == comp:
        await bot.send_message(message.from_user.id, f"Ничья {user}:{comp}")
    else: 
        await bot.send_message(message.from_user.id, f"Ты проиграл компьютер: {comp}, ты: {user}")



async def get_random_user(message: types.Message):
    await sql_command_random(message)


async def parser_cartoons(message: types.Message):
    items = cartoons.parser()
    for item in items:
        await message.answer(
            f"{item['link']}\n"
            f"{item['title']}\n"
            f"{item['status']}\n"
            f"#Y{item['year']}\n"
            f"#{item['country']}\n"
            f"#{item['genre']}\n"
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(starthandler, commands=['start', 'help'])
    dp.register_message_handler(sendQuiz1, commands=['quiz'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(dice_game, commands=['dice'])
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_message_handler(parser_cartoons, commands=['cartoon'])