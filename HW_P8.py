# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной """




import json


welcome = 'Enter command: 1 - read & show | 2 - add record | 3 - search | 4 - init DB | q - Quit\n'
phone_book = {}
db_path = 'phone_book.json'

def print_book(book):
    for k,v in book.items():
        print (k," - ", end = " | ")
        for i,j in v.items():
            print (i, j, end = " | ")
        print()

def add_record(book):
    k=input("Put new name")
    a={}
    a['phone']=list(input('put phone').split())
    a['birthday']=input('put birthday')
    a['email']=input('put email')
    book[k]=a

def save_db(path, db):
    with open(path, 'w', encoding='utf-8') as fh: # открываем файл на запись
        fh.write(json.dumps(db, ensure_ascii=False)) # преобразовываем словарь data в unicode-строку и записываем в файл
        print('БД успещно сохранена')

def load_db(path):
            # загрузить из json
            with open(path, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                BD_local = json.load(fh)  # загружаем из файла данные в словарь data
            print('БД успещно загружена')
            return BD_local
try:
    phone_book = load_db(db_path)
except:
    phone_book = {
    'Миша гараж':{'phone': ['72443351195','72627397543'] , 'birthday': '11-02-2010', 'email':"mail@mail.ru"},
    'Sasha':{'phone': ['78436840045','77554802591']}}
    print('Not found. Create Base')                 

action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        print_book(phone_book)
    elif action == '2':
        add_record (db_path, phone_book)
    elif action == '3':
         load_db (phone_book)
    elif action == '4':
        save_db(db_path, phone_book)
save_db(db_path,phone_book)
