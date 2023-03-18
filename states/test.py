from aiogram.dispatcher.filters.state import StatesGroup, State

class new_event(StatesGroup):
    id_club = State()
    name_event = State()
    description_event = State()
    link_event = State()
    date_event = State()
    time_event = State()
    place_event = State()
    answer_question = State()
    update_name = State()
    update_description = State()
    update_link = State()
    update_date = State()
    update_time = State()
    update_place = State()

class rename_event(StatesGroup):
    edit_name = State()
    edit_answer_question = State()
    edit_description = State()
    edit_link = State()
    edit_date = State()
    edit_time = State()
    edit_place = State()