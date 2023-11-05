from aiogram import executor
from config import dp
import logging
from handlers import client, callback, extra, admin

client.register_handlers_client(dp)
callback.register_hendlers_callback(dp)
extra.register_handlers_extra(dp)
admin.register_admin_handlers(dp)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)
