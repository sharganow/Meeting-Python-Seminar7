main_menu = [
    '---\nСписок возможных действий с телефонным справочником: ',
    'Показать все контакты',
    'Открыть файл',
    'Сохранить файл',
    'Создать контакт',
    'Изменить контакт',
    'Удалить контакт',
    'Выход.\n---'
]
new_contact = [
    'Создавая запись нового контакта заполните следующие поля: ',
    'Фамилия',
    'Имя',
    'Номер телефона',
    'Тип номера',
    'Сохранить',
    'Отменить'
]
change_contact = [
    'Изменяя запись контакта поменяйте следующие поля: ',
    'Фамилия',
    'Имя',
    'Номер телефона',
    'Тип номера',
    'Сохранить',
    'Отменить'
]
query_exit = [
    'Записи в телефонном справочнике изменены, перед завершением программы,\nвыберите действие, которое нужно совершить с изменениями: ',
    'Сохранить изменения, а потом выйти из программы',
    'Отменить изменения и выйти из программы'
]


def show_menu(lst: list):
    print(f'{lst[0]}')
    for i, d in enumerate(lst[1:]):
        s = ';' if i < len(lst) - 2 else ' '
        print(f'\t{i + 1}. {d}{s}')


def get_user_choice(lst: list) -> str:
    choise = 0
    show_menu(lst)
    while True:
        try:
            choice = int(input('Выберите желаемое действие из приведённого выше списка: '))
            if 0 < choice < len(lst):
                break
            else:
                print('Ваш выбор выходит за пределы предложенных вариантов')
                show_menu(lst)
        except:
            print('Значение должно быть целым числом из диапазона предлагаемых вариантов')
            show_menu(lst)
    return lst[choice]


def show_all_contacts(db: list):
    print('Список всех контактов существующих в телефонном справочнике:')
    if len(db) == 0:
        print('Телефонная книга не открыта или пуста')
    else:
        for i, d in enumerate(db):
            print(f'\t{i + 1}. ', end='')
            for value in d.values():
                print(f'{value} ', end='')
            print()


def show_changing_contact(ind: int, cell: list) -> None:
    if len(cell) != 4:
        print('Ячейка записи имеет неверный формат - произошел сбой')
    else:
        print(f'\t{ind + 1}. ', end='')
        for value in cell.values():
            print(f'{value} ', end='')
        print()


def phonebook_opened() -> None:
    print('Телефонная книга открыта')


def report_close_db(report: int) -> None:
    match report:
        case 0:
            print('Телефонная книга не открыта или пуста')
        case 1:
            print('Телефонная книга сохранена')
        case 2:
            print('Проблема в имени файла телефонной книги')


def enter_field_contact(lst: list, field: str) -> list:
    if len(lst) == 4:
        match field:
            case 'Фамилия':
                lst[0] = input('Введите фамилию: ')
            case 'Имя':
                lst[1] = input('Введите имя: ')
            case 'Номер телефона':
                lst[2] = input('Введите номер телефона: ')
            case 'Тип номера':
                lst[3] = input('Введите тип номера: ')
            case _:
                print('В установленом формате тип поля неизвестен - произошел сбой')
    else:
        print('Количество полей не соответствует установленному формату - произошел сбой')
    return lst


def report_add_new_contact(report: int) -> None:
    match report:
        case 0:
            print('Новый контакт добавлен')
        case 1:
            print('Новый контакт не был добавлен')
        case 2:
            print('Телефонная книга не открыта или пуста')


def report_change_contact(report: int) -> None:
    match report:
        case 0:
            print('Контакт изменён')
        case 1:
            print('Контакт не был изменён')
        case 2:
            print('Телефонная книга не открыта или пуста')


def get_record_choice(db: list) -> int:
    choise = 0
    show_all_contacts(db)
    while True:
        try:
            choice = int(input('Из выденного списка выберите запись, которую желаете изменить: '))
            if 0 < choice <= len(db):
                break
            else:
                print('Ваш выбор выходит за пределы предложенных вариантов')
                show_all_contacts(db)
        except:
            print('Значение должно быть целым числом из диапазона предлагаемых вариантов')
            show_all_contacts(db)
    return choice - 1


def change_field_contact(lst: list, field: str) -> list:
    if len(lst) == 4:
        match field:
            case 'Фамилия':
                lst['Фамилия'] = input('Введите новую фамилию: ')
            case 'Имя':
                lst['Имя'] = input('Введите новое имя: ')
            case 'Номер телефона':
                lst['Номер телефона'] = input('Введите новый номер телефона: ')
            case 'Тип номера':
                lst['Тип номера'] = input('Скорректируйте тип номера: ')
            case _:
                print('В установленом формате тип поля неизвестен - произошел сбой')
    else:
        print('Количество полей не соответствует установленному формату - произошел сбой')
    return lst