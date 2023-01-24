list_command = [
    'Список возможных действий с телефонным справочником: ',
    'Показать все контакты',
    'Открыть файл',
    'Сохранить файл',
    'Создать контакт',
    'Изменить контакт',
    'Удалить контакт',
    'Выход'
]


def show_menu(lst: str):
    print(f'{lst[0]}')
    for i, d in enumerate(lst[1:]):
        s = ';' if i < len(lst) - 1 else '.'
        print(f'\t{i + 1}. {d}{s}')


def get_user_choice(lst: str) -> int:
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
    return choice


def show_all_contacts(db: list):
    print('Список всех контактов существующих в телефонном справочнике:')
    for i, d in enumerate(db):
        print(f'\t{i+1}. ', end='')
        for value in d.values():
            print(f'{value} ', end='')
        print()