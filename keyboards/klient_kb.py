from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

start_button = KeyboardButton("/start")
info_button= KeyboardButton("/info")
quiz_button = KeyboardButton("/quiz")
dice_button = KeyboardButton('/dice')
reg_button = KeyboardButton('/reg')

share_location = KeyboardButton("Share Location", request_location=True)
share_contact = KeyboardButton("Share Contact", request_contact=True)


start_markup.add(start_button, info_button, quiz_button, share_location, share_contact, dice_button, reg_button)


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton('ДА'),
    KeyboardButton('НЕТ')
)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton('CANCEL'),
)



gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
).add(
    KeyboardButton('Man'),
    KeyboardButton('Women'),
    KeyboardButton("I don't know"),
    KeyboardButton("CANCEL"),
)