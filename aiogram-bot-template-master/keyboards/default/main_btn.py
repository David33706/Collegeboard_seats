from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

m = ''
def Beta():
    m = ReplyKeyboardMarkup(resize_keyboard=True)
    m.add(KeyboardButton('Show all test centers'))
    m.add(KeyboardButton('Show individual test center'))
    m.add(KeyboardButton('Return to choosing date⬅️'))
    return m

def seat_emoji(d):
    if d == "Full, no seats":
        d += '❌'
    else:
        d += '✅'
    return d
def country_emoji(ctr):
    if ctr == "Uzbekistan":
        return "Uzbekistan 🇺🇿"
    if ctr == "Kazakhstan":
        return "Kazakhstan 🇰🇿"
    if ctr == "Kyrgyzstan":
        return "Kyrgyzstan 🇰🇬"
def date_emoji(date):
    return date+" 📆"

# Date Buttons


button_MR = KeyboardButton('March 11')
button_MY = KeyboardButton('May 6')
button_JN = KeyboardButton('June 3')
button_DC = KeyboardButton('Dec 3')

button_HP = KeyboardButton('Help!')

# Country Buttons
button_CTR = KeyboardButton('Change country')
button_UZ = KeyboardButton('Uzbekistan 🇺🇿')
button_KZ = KeyboardButton('Kazakhstan 🇰🇿')
button_KR = KeyboardButton('Kyrgyzstan 🇰🇬')
# Adding those buttons
# Country
ctry_markup = ReplyKeyboardMarkup(resize_keyboard=True)
ctry_markup.row(button_UZ,button_KZ,button_KR)
# Date
data_markup = ReplyKeyboardMarkup(resize_keyboard=True)
data_markup.row(button_MR,button_MY,button_JN).add(button_CTR, button_HP)
a = ''
