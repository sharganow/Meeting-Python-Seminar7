import time
import view as vw
import model as ml

last_choice = 0

while True:
    try:
        match last_choice:
            case 0:
                last_choice = vw.get_user_choice(vw.list_command)
            case 1:
                vw.show_all_contacts(ml.read_db('phonebook.phn'))
                last_choice = 0
                time.sleep(5)
            case 7:
                break
            case _:
                last_choice = 0
    except:
        print('Что-то пошло не так')
        last_choice = vw.get_user_choice(vw.list_command)
