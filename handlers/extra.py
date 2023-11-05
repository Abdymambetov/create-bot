from aiogram import types, Dispatcher
from config import dp, bot


# DRY - Don't repeat your self
# @dp.message_handler()
async def echo(message: types.Message):
    print(message)
    bad_words = ['lox', 'pidr', 'stupid', 'mat']
    username = f"@{message.from_user.username}" if message.from_user.username is not None else message.from_user.full_name
    # if message.from_user.username is not None:
    #     username = f"@{message.from_user.username}"
        
    for word in bad_words:
        if word in message.text.lower():
            await message.reply(f"не матерись, {username}! сам ты {word}")

    if message.text.startswith('!'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text == 'dice':
        num = await bot.send_dice(message.chat.id, emoji='🎲')
        print(num.dice.value)

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)