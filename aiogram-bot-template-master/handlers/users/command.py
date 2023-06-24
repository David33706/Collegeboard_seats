from aiogram import types
from loader import dp, db
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.default.main_btn import ctry_markup, data_markup
from keyboards.default.main_btn import Beta, country_emoji, date_emoji, seat_emoji
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from states.main_state import countryname, center_avaibility

# @dp.message_handler(commands=['start', 'help'], state=None)
# async def starting(message: types.Message):
#     await message.answer(
#         "This is collegeboard bot.\nIts main purpose to help you check if seats for the chosen date are avialable\nPlease choose preferable country and test date",
#         reply_markup=ctry_markup)
#     name = message.from_user.full_name
#     # Foydalanuvchini bazaga qo'shamiz
#     try:
#         db.add_user(id=message.from_user.id,
#                     name=name)
#     except sqlite3.IntegrityError as err:
#         await bot.send_message(chat_id=ADMINS[0], text=err)
#
#     # Adminga xabar beramiz
#     count = db.count_users()[0]
#     msg = f"{message.from_user.full_name} added to the base.\n {count} users in the bot."
#     await bot.send_message(chat_id=ADMINS[0], text=msg)
#     await countryname.country.set()
dt_hr = {}


@dp.message_handler(state=countryname.country)
async def nm(message: types.Message, state: FSMContext):
    if message.text == "Uzbekistan 🇺🇿" or message.text == "Kazakhstan 🇰🇿":
        # Writing country name inside file
        f = open('/home/Collegeboard_project/countryname.txt', 'w')
        f.write(message.text[0:-3])
        f.close()
        await message.answer('Alright we choose country', reply_markup=data_markup)
        await state.finish()
    else:
        await message.answer('Please choose country from the list', reply_markup=ctry_markup)
        pass


# User details
@dp.message_handler(state=None)
async def data(message: types.Message):
    # Executing country info
    if message.text == "Change country":
        await message.answer('Okay. We will change the country', reply_markup=ctry_markup)
        await countryname.country.set()
    # Dates
    # Execute function everything when get date

    if message.text == "March 11":
        d = open('/home/Collegeboard_project/date.txt', 'w')
        d.write('March')
        d.close()
        await message.answer('Alright, choose the test center', reply_markup=Beta())
        await center_avaibility.center.set()
    if message.text == "May 6":
        d = open('/home/Collegeboard_project/date.txt', 'w')
        d.write('May')
        d.close()
        await message.answer('Alright, choose the test center', reply_markup=Beta())
        await center_avaibility.center.set()
    if message.text == "June 3":
        d = open('/home/Collegeboard_project/date.txt', 'w')
        d.write('June')
        d.close()
        await message.answer('Alright, choose the test center', reply_markup=Beta())
        await center_avaibility.center.set()
    # Help info
    if message.text == "Help!":
        await message.answer(
            "Please choose preferable test date\nthat you want register by clicking\ntest date buttons",
            reply_markup=data_markup)


@dp.message_handler(state=center_avaibility.center)
async def ct(message: types.Message, state: FSMContext):
    try:
        # Reading country name and date
        shw = ''
        m = ReplyKeyboardMarkup(resize_keyboard=True)

        country_file = open('/home/Collegeboard_project/countryname.txt', 'r')
        date_file = open('/home/Collegeboard_project/date.txt', 'r')
        ctr = country_file.read()
        date = date_file.read()
        # Creating path
        name = '/home/Collegeboard_project/' + ctr + '/' + date + '_' + ctr + '.txt'
        f = open(name, 'r')
        # Making txt list
        ft = f.read()
        a = ft.split('\n\n')
        d = {}

        for i in a:
            if '\n' in i:
                n = i.split('\n')
                # Adding dict center and aviability
                d[n[0]] = n[1]
                loc = '\nLocation📍: ' + n[2]
                dt_hr.update({n[0]: loc})
                gog_map = '\n' + n[3]
                dt_hr.update({n[0] + 'gog': gog_map})
        # Last time checked
        dt_hr['hour'] = a[-1]
        if message.text == 'Show individual test center':
            m.add(KeyboardButton('Back⬅️'))
            for i in a:
                if '\n' in i:
                    # If '\n' inside an object, make it button
                    n = i.split('\n')
                    k = KeyboardButton(n[0])
                    m.add(k)
            m.add(KeyboardButton('Return to choosing date⬅️'))
            await message.answer('Alright choose individual test centers', reply_markup=m)
            await center_avaibility.next()
        # if message.text in d:
        #     # When center is in text
        #     await message.answer(
        #         ctr + '\n' + date + '\n\n' + message.text + '\n' + seat_emoji(d.get(message.text)) +dt_hr[message.text]+ '\n\n' + dt_hr['hour'])
        # If you user wants to exit
        if message.text == 'Return to choosing date⬅️':
            await message.answer('Okay, we will return to choosing date', reply_markup=data_markup)
            await state.finish()
        # If you want to show all test centers
        if message.text == "Show all test centers":

            shw += country_emoji(ctr) + '\n'
            shw += date_emoji(date) + '\n'
            for i in d:
                shw += '\n' + i + '\n' + seat_emoji(d.get(i)) + dt_hr[i] + dt_hr[i + 'gog']
                shw += '\n'
            shw += '\n' + dt_hr['hour']
            await message.answer(shw)

        # Closing all files
        date_file.close()
        country_file.close()
        f.close()
    except:
        await message.answer("You choose wrong button or sent wrong text")
        pass


@dp.message_handler(state=center_avaibility.individual_center)
async def ct(message: types.Message, state: FSMContext):
    try:
        country_file = open('/home/Collegeboard_project/countryname.txt', 'r')
        date_file = open('/home/Collegeboard_project/date.txt', 'r')
        ctr = country_file.read()
        date = date_file.read()
        # Creating path
        name = date + '_' + ctr + '.txt'
        name = '/home/Collegeboard_project/' + ctr + '/' + date + '_' + ctr + '.txt'
        f = open(name, 'r')
        # Making txt list
        ft = f.read()
        a = ft.split('\n\n')
        d = {}
        for i in a:
            if '\n' in i:
                n = i.split('\n')
                # Adding dict center and aviability
                d[n[0]] = n[1]
                loc = '\nLocation📍: ' + n[2]
                dt_hr.update({n[0]: loc})
                gog_map = '\n' + n[3]
                dt_hr.update({n[0] + 'gog': gog_map})
        # Last time checked
        dt_hr['hour'] = a[-1]
        if message.text in d:
            # When center is in text
            await message.answer(
                country_emoji(ctr) + '\n' + date_emoji(date) + '\n\n' + message.text + '\n' + seat_emoji(
                    d.get(message.text)) + dt_hr[message.text] + dt_hr[message.text + 'gog'] + '\n\n' + dt_hr['hour'])
        if message.text == 'Back⬅️':
            await message.answer('Okay', reply_markup=Beta())
            await state.finish()
            await center_avaibility.center.set()
        if message.text == 'Return to choosing date⬅️':
            await message.answer('Okay, we will return to choosing date', reply_markup=data_markup)
            await state.finish()


    except:
        await message.answer("You choose wrong button or sent wrong text")
        pass


@dp.message_handler(text="/start", state=center_avaibility.center)
async def ct(message: types.Message, state: FSMContext):
    await message.answer('Okay', reply_markup=data_markup)
    await state.finish()


@dp.message_handler(text="/start", state=center_avaibility.individual_center)
async def ct(message: types.Message, state: FSMContext):
    await message.answer('Okay', reply_markup=data_markup)
    await state.finish()
