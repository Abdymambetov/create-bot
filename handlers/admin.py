from aiogram import types, Dispatcher
from config import dp, bot, ADMINS
from database.bot_db import sql_command_delete, sql_command_all, sql_command_get_all_ids
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def banUser(message: types.Message):
    user = f"{message.from_user.username}" if message.from_user.username is not None else message.from_user.first_name
    if message.chat.type == 'group':
        if message.from_user.id not in ADMINS:
            await message.answer('Ты не мой босс!')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение!')
        else: 
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id,)
            await message.answer(f"{user} - братишка f'забанил {message.reply_to_message.from_user.full_name}' ")

            # await bot.ban_chat_member() - бан человека, kick_chat_member - выкидывает из группы
    else: 
        await message.answer('Пиши в группе!')


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer('Ты не мой босс!')
    else:
        users = await sql_command_all()
        for user in users:
           await bot.send_photo(message.from_user.id, user[6], 
                            caption=f"{user[2]}, {user[3]}, {user[4]}, {user[5]},\n {user[1]}",
                            reply_markup=InlineKeyboardMarkup().add(
                                InlineKeyboardButton(f'delete{ user[2]}',
                                                    callback_data=f"delete {user[0]}")
                            )
                        )

async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text='Удалено', show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)



async def newsletter(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer('Ты не мой босс!')
    else:
        user_ids = await sql_command_get_all_ids()
        for user_id in user_ids:
            await bot.send_message(user_id[0], message.text.replace('/R', ''))


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(banUser, commands=['ban'], commands_prefix="!/")
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_message_handler(newsletter, commands=['R'])
    dp.register_callback_query_handler(complete_delete, 
                                    lambda call: call.data and call.data.startswith("delete "))