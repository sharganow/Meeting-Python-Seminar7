main_menu = [
    'Список возможных действий с телефонным справочником: ',
    'Показать все контакты',
    'Открыть файл',
    'Сохранить файл',
    'Создать контакт',
    'Изменить контакт',
    'Удалить контакт',
    'Выход'
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


def show_menu(lst: list):
    print(f'{lst[0]}')
    for i, d in enumerate(lst[1:]):
        s = ';' if i < len(lst) - 1 else '.'
        print(f'\t{i + 1}. {d}{s}')


def get_user_choice(lst: list) -> int:
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
            print('Новый контакт не был добавлен')
        case 1:
            print('Новый контакт добавлен')
        case _:
            print('Состояние добавления нового контакто неизвестно - произошел сбой')


def report_change_contact(report: int) -> None:
    match report:
        case 0:
            print('Контакт изменён')
        case 1:
            print('Контакт не был изменён')
        case 2:
            print('Телефонная книга не открыта или пуста')


def get_record_choice(db: list) -> int:
    show_all_contacts(db)
    print('Из выденного списка выберите запись, которую желаете изменить: ')