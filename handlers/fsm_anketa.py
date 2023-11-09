from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from keyboards.klient_kb import submit_markup, cancel_markup, gender_markup


#FSM- Finito State Machine

class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    region = State()
    photo = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer('what is your name?', reply_markup=cancel_markup)
    else: 
        await message.answer('Write private message')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}"
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('What is your age?')
    

async def load_age(message: types.Message, state: FSMContext):
    try:
        if 16 < int(message.text) < 50:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMAdmin.next()
            await message.answer('What is your gender?', reply_markup=gender_markup)
        else:
            await message.answer('Access is denied!')
    except:
        await message.answer('Write properly')
    


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
    await FSMAdmin.next()
    await message.answer('What is your region?', reply_markup=cancel_markup)
    
async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
    await FSMAdmin.next()
    await message.answer('Send your photo')
    
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await bot.send_photo(message.from_user.id, data['photo'], 
                            caption=f"{data['name']}, {data['age']}, {data['gender']}, {data['region']},\n {data['username']}")
        print(data)
    await FSMAdmin.next()
    await message.answer('Is everything filled out correctly?', reply_markup=submit_markup)

async def submit_correct(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        #В базу данных
        await state.finish()
        await message.answer("You are registered!")
    elif message.text.lower == 'нет':
        await state.finish()
        await message.answer("cancle")
    else: 
        await message.answer('What!?')


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None: 
        await state.finish()
        await message.answer('Cancel!')
    


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(submit_correct, state=FSMAdmin.submit)



