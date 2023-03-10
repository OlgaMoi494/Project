'''4. Прочитать сохранённый json-файл и записать данные на диск в csv-файл,
первой строкой которого озоглавив каждый столбец и добавив новый столбец
"телефон".'''

import csv
import json
from random import randint

with open('json_file.json', 'r') as jf:
    js_content = jf.read()
    data_dict = json.loads(js_content)  # читаем json файл, получаем словарь


def random_3num() -> str:
    '''Возвращает 3 произвольных цифры в строковом формате'''
    return ''.join(list(map(str, [randint(0, 9) for _ in range(3)])))


data_lst = []
for key, value in data_dict.items():
    new_phone = '(00)' + random_3num() + '-' + random_3num()
    value.insert(0, key)
    value.append(new_phone)
    data_lst.append(value)
    # из словаря делаем список и добавляем произвольный телефон

data_lst.insert(0, ['id', 'name', 'age', 'phone'])  # добавляем заголовки

with open('csv_file.csv', 'w', newline='') as csvf:
    csvf_writer = csv.writer(csvf)

    for row in data_lst:
        csvf_writer.writerow(row)  # записываем в csv
