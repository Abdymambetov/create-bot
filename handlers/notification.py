from aioschedule import every, run_pending
from aiogram import types, Dispatcher
from config import bot
from asyncio import sleep

async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer('OK!')


async def go_to_sleep():
    await bot.send_message(
        chat_id=chat_id,
        text="Иди спать!"
    )

async def wake_up():
    video = open('assets/video.mp4', 'rb')
    await bot.send_video(
        chat_id=chat_id,
        video=video
    )

async def scheduler():
    every().day.at("15:18").do(go_to_sleep)
    every().day.at("14:49").do(wake_up)
    while True:
        await run_pending()
        await sleep(2)

# def sync_scheduler():
#     every().day.at("15:24").do(go_to_sleep)
#     # every().day.at("14:49").do(wake_up)

# async def scheduler():
#     while True:
#         await run_pending()
#         await sleep(2)

def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, 
                                lambda word: 'notify' in word.text)





