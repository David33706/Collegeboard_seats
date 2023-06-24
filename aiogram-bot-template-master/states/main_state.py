from aiogram.dispatcher.filters.state import State, StatesGroup
class countryname(StatesGroup):
    country = State()


# Class for center naming
class center_avaibility(StatesGroup):
    center = State()
    individual_center = State()