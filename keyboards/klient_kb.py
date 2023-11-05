from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

start_button = KeyboardButton("/start")
info_button= KeyboardButton("/info")
quiz_button = KeyboardButton("/quiz")

share_location = KeyboardButton("Share Location", request_location=True)
share_contact = KeyboardButton("Share Contact", request_contact=True)


start_markup.add(start_button, info_button, quiz_button, share_location, share_contact)