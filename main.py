from aiogram import executor
from config import dp
import logging
from handlers import client, callback, extra, admin, fsm_anketa, notification
from database.bot_db import sql_create
from asyncio import create_task


async def on_start_up(_):
    create_task(notification.scheduler())
    # await notification.scheduler()
    # notification.sync_scheduler()
    sql_create()


client.register_handlers_client(dp)
callback.register_hendlers_callback(dp)
extra.register_handlers_extra(dp)
admin.register_admin_handlers(dp)
fsm_anketa.register_handlers_fsm_anketa(dp)
notification.register_handler_notification(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False, on_startup=on_start_up)
