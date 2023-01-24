import time
import view as vw
import model as ml

delay = 2


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
                case 'Выход':
                    break
                case _:
                    last_choice = 'Main menu'
        except:
            print('Что-то пошло не так')
        time.sleep(delay)


def new_contact(menu: list) -> int:
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
                    return 1
                case 'Отменить':
                    break
        except:
            print('Что-то пошло не так')
        time.sleep(delay)
    return 0


def change_contact(db: list) -> int:
    if len(db) == 0:
        return 2
    last_choice = 'Main menu'
    while True:
        try:
            match last_choice:
                case 'Main menu':
                    vw.show_all_contacts(db)
                case ('Фамилия') | ('Имя') | ('Номер телефона') | ('Тип номера'):
                    contact = vw.enter_field_contact(contact, last_choice)
                    list_menu.pop(list_menu.index(last_choice))
                    last_choice = 'Main menu'
                case 'Сохранить':
                    ml.add_new_contact(contact)
                    return 1
                case 'Отменить':
                    break
        except:
            print('Что-то пошло не так')
        time.sleep(delay)
    return 0