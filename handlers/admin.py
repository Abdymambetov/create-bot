from aiogram import types, Dispatcher
from config import dp, bot, ADMINS

async def banUser(message: types.Message):
    user = f"{message.from_user.username}" if message.from_user.username is not None else message.from_user.first_name
    if message.chat.type == 'group':
        if message.from_user.id in ADMINS:
            await message.answer('Ты не мой босс!')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение!')
        else: 
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id,)
            await message.answer(f"{user} - братишка f'забанил {message.reply_to_message.from_user.full_name}' ")

            # await bot.ban_chat_member() - бан человека, kick_chat_member - выкидывает из группы
    else: 
        await message.answer('Пиши в группе!')



def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(banUser, commands=['ban'], commands_prefix="!/")