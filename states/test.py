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

class name_club(StatesGroup):
    club_name = State()
    edit_club_name = State()
    ID_edit_club_name = State()
    ID_club_delete = State()

class reg_admin(StatesGroup):
    admin_id = State()
    first_name = State()
    last_name = State()
    username = State()
    fio_admin = State()
    vk_link_admin = State()
    ID_club_admin = State()
    admin_position = State()
    answer_question_admin = State()
    update_fio_admin = State()
    update_vk_link_admin = State()
    update_ID_club_admin = State()
    add_admin = State()

class reg_yes_no_admin(StatesGroup):
    add_admin = State()
    not_add_admin = State()

