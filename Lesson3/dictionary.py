"""Способы создания словаря"""
new_dict = {'a': 'b'}
new_dict1 = dict(c='d')
new_dict2 = dict.fromkeys(['a', 'b'], 'c')  # assign a default value to several keys
new_dict3 = dict([('key1', 'key2'), ('val1', 'val2')])
print(new_dict, new_dict1, new_dict2, new_dict3, '\n')

import random

lst_choice = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
lst_created = [random.choice(lst_choice) for _ in range(20)]
print(lst_created)
new_dict4 = {i: lst_created.count(i) for i in lst_choice}  # создание словаря методом включений
print(new_dict4, '\n')

""""Методы словаря"""
new_dict5 = new_dict.copy()  # копирование словаря
print(new_dict, new_dict.get('c'))  # dict.get() получение значения по ключу, при отсутcвии ключа выводит None
new_dict6 = {'a': 1, 'b': 2, 'c': 3}
new_dict7 = {v: k for k, v in new_dict6.items()}  # dict.items() используется в циклах
print(new_dict6, new_dict7)  # ключи и значения поменяли местами
print(new_dict6.pop('d', 'no key'))  # dict.pop(key, default) удаляет и возвращает значение по ключу,
# если нет ключа - default
popped_item = new_dict6.popitem()  # dict.popitem() удаляет последнюю пару ключ, значение и возвращает в виде кортежа
dict_with_popped_items = {popped_item[0]: popped_item[1]}
print(dict_with_popped_items, new_dict6)
new_dict6.setdefault('c',
                     100)  # dict.setdefault(key, default) меняет объект, если нет ключа, то дабавляет новый ключ - знач
print(new_dict6)
new_dict6.update(new_dict7)  # dict.update(other_dict) меняет объект, добавляет е нему второй словарь
print(new_dict6)
print(new_dict6.values())  # dict.values() возвращает значения
print(new_dict6.keys())  # dict.keys() возвращает ключи
