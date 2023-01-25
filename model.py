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
        if len(d) == 4:
            db = dict()
            db['Фамилия'] = d[0]
            db['Имя'] = d[1]
            db['Номер телефона'] = d[2]
            db['Тип номера'] = d[3]
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
                strn += value + ';'
            strn = strn[:-1] + '\n'
            my_phonebook += strn
        try:
            with open(path, 'w', encoding='UTF-8') as file:
                file.write(my_phonebook[:-1])
        except:
            return 2
        list_dbl = list()
        set_db(list_dbl)
        return 1


def add_new_contact(lst: list) -> None:
    if len(lst) == 4:
        dbl = get_db()
        db = dict()
        db['Фамилия'] = lst[0]
        db['Имя'] = lst[1]
        db['Номер телефона'] = lst[2]
        db['Тип номера'] = lst[3]
        dbl.append(db)
        set_db(dbl)


def compare_two_listcontact(old: list, new: list) -> int:
    if len(old) != len(new):
        return 0
    else:
        for i in range(len(old)):
            listoldkeys = [j for j in old[i].keys()]
            listnewkeys = [j for j in new[i].keys()]
            listoldvalues = [j for j in old[i].values()]
            listnewvalues = [j for j in new[i].values()]
            if len(listoldkeys) != len(listnewkeys) != len(listoldvalues) != len(listnewvalues):
                return 0
            else:
                for k in range(len(listoldkeys)):
                    if listoldkeys[k] != listnewkeys[k]:
                        return 0
                    else:
                        if listoldvalues[k] != listnewvalues[k]:
                            return 0
        else:
            return 1


