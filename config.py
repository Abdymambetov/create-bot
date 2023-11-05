from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot)
ADMINS = [1259986211]