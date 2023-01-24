list_db = list()


def read_db(path: str) -> list:
    global list_db
    my_phonebook = str
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            my_phonebook = file.read()
    except:
        print('Проблема в имени файла телефонного справочника')
        return []
    my_phonebook = [[word for word in strn.strip().split(';')] for strn in my_phonebook.split('\n')]
    for i, d in enumerate(my_phonebook):
        db = dict()
        db['lastname'] = d[0]
        db['firstname'] = d[1]
        db['phone.append'] = d[2]
        db['phone_comment.append'] = d[3]
        list_db.append(db)
    return list_db
