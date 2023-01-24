list_db = list()


def get_db() -> list:
    global list_db
    return list_db


def set_db(db: list) -> None:
    global list_db
    list_db = db[:]


def open_db(path: str) -> list:
    open_dbl = list()
    my_phonebook = str
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            my_phonebook = file.read()
    except:
        return []
    my_phonebook = [[word for word in strn.strip().split(';')] for strn in my_phonebook.split('\n')]
    for i, d in enumerate(my_phonebook):
        db = dict()
        db['lastname'] = d[0]
        db['firstname'] = d[1]
        db['phone.append'] = d[2]
        db['phone_comment.append'] = d[3]
        open_dbl.append(db)
    return open_dbl


def close_db(path: str) -> int:
    list_dbl = get_db()
    if len(list_dbl) == 0:
        return 0
    else:
        my_phonebook = ''
        for i, d in enumerate(list_dbl):
            strn = ''
            for value in d.values():
                strn += value + ' '
            strn = strn.strip().replace(' ', ';')
            strn += '\n'
            my_phonebook += strn
        try:
            with open(path, 'w', encoding='UTF-8') as file:
                file.write(my_phonebook[:-1])
        except:
            return 2
        list_dbl = list()
        set_db(list_dbl)
        return 1
