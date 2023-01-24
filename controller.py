import time
import view as vw
import model as ml

delay = 2
last_choice = 0


def execute() -> None:
    global last_choice
    while True:
        try:
            match last_choice:
                case 0:
                    last_choice = vw.get_user_choice(vw.list_command)
                case 'Показать все контакты':
                    vw.show_all_contacts(ml.get_db())
                    last_choice = 0
                    time.sleep(delay)
                case 'Открыть файл':
                    ml.set_db(ml.open_db('phonebook.phn'))
                    vw.phonebook_opened()
                    last_choice = 0
                    time.sleep(delay)
                case 'Сохранить файл':
                    vw.report_close_db(ml.close_db('phonebook.phn'))
                    last_choice = 0
                    time.sleep(delay)
                case 'Создать контакт':

                    last_choice = 0
                    time.sleep(delay)
                case 'Выход':
                    break
                case _:
                    last_choice = 0
        except:
            print('Что-то пошло не так')
            last_choice = vw.get_user_choice(vw.list_command)
