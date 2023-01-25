import time
import view as vw
import model as ml

delay = 1


def main_menu() -> None:
    last_choice = 'Main menu'
    while True:
        try:
            match last_choice:
                case 'Main menu':
                    last_choice = vw.get_user_choice(vw.main_menu)
                case 'Показать все контакты':
                    vw.show_all_contacts(ml.get_db())
                    last_choice = 'Main menu'
                case 'Открыть файл':
                    ml.set_db(ml.open_db('phonebook.phn'))
                    vw.phonebook_opened()
                    last_choice = 'Main menu'
                case 'Сохранить файл':
                    vw.report_close_db(ml.close_db('phonebook.phn'))
                    last_choice = 'Main menu'
                case 'Создать контакт':
                    vw.report_add_new_contact(new_contact(vw.new_contact))
                    last_choice = 'Main menu'
                case 'Изменить контакт':
                    vw.report_change_contact(change_contact(ml.get_db()))
                    last_choice = 'Main menu'
                case 'Удалить контакт':
                    vw.report_delete_contact(delete_contact(ml.get_db()))
                    last_choice = 'Main menu'
                case 'Выход.\n---':
                    if ml.compare_two_listcontact(ml.open_db('phonebook.phn'), ml.get_db()):
                        break
                    else:
                        if len(ml.get_db()) != 0:
                            save_exit()
                        break
                case _:
                    last_choice = 'Main menu'
        except:
            vw.something_wron
        time.sleep(delay)


def new_contact(menu: list) -> int:
    db = ml.get_db()
    if len(db) == 0:
        return 2
    last_choice = 'Main menu'
    list_menu = menu[:]
    contact = [' ', ' ', ' ', ' ']
    while True:
        try:
            match last_choice:
                case 'Main menu':
                    last_choice = vw.get_user_choice(list_menu)
                case ('Фамилия') | ('Имя') | ('Номер телефона') | ('Тип номера'):
                    contact = vw.enter_field_contact(contact, last_choice)
                    list_menu.pop(list_menu.index(last_choice))
                    last_choice = 'Main menu'
                case 'Сохранить':
                    ml.add_new_contact(contact)
                    return 0
                case 'Отменить':
                    break
        except:
            vw.something_wron
        time.sleep(delay)
    return 1


def change_contact(db: list) -> int:
    if len(db) == 0:
        return 2
    last_choice = 'Choose the record'
    change_menu = vw.change_contact[:]
    cell = list()
    index = -1
    while True:
        try:
            match last_choice:
                case 'Choose the record':
                    index = vw.get_record_change(db)
                    cell = db[index]
                    last_choice = 'Change menu'
                case 'Change menu':
                    vw.show_changing_contact(index, cell)
                    last_choice = vw.get_user_choice(change_menu)
                case ('Фамилия') | ('Имя') | ('Номер телефона') | ('Тип номера'):
                    cell = vw.change_field_contact(cell, last_choice)
                    change_menu.pop(change_menu.index(last_choice))
                    last_choice = 'Change menu'
                case 'Сохранить':
                    db[index] = cell
                    ml.set_db(db)
                    return 0
                case 'Отменить':
                    break
        except:
            vw.something_wrong()
        time.sleep(delay)
    return 1


def delete_contact(db: list) -> int:
    if len(db) == 0:
        return 2
    last_choice = 'Choose the record'
    delete_menu = vw.delete_contact[:]
    cell = list()
    index = -1
    while True:
        try:
            match last_choice:
                case 'Choose the record':
                    index = vw.get_record_delete(db)
                    cell = db[index]
                    last_choice = 'Change menu'
                case 'Change menu':
                    vw.show_changing_contact(index, cell)
                    last_choice = vw.get_user_choice(delete_menu)
                case 'Удалить контакт':
                    cell = db.pop(index)
                    ml.set_db(db)
                    return 0
                case 'Сохранить контакт':
                    break
        except:
            vw.something_wrong()
        time.sleep(delay)
    return 1


def save_exit():
    last_choice = 'Main menu'
    list_menu = vw.query_exit[:]
    while True:
        try:
            match last_choice:
                case 'Main menu':
                    last_choice = vw.get_user_choice(list_menu)
                case 'Сохранить изменения, а потом выйти из программы':
                    vw.report_close_db(ml.close_db('phonebook.phn'))
                    break
                case 'Отменить изменения и выйти из программы':
                    break
        except:
            vw.something_wron
        time.sleep(delay)
