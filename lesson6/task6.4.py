from time import sleep
from datetime import datetime

def time_print():
    """Возвращает текущий момент datetime в формате строки по шаблону"""
    time_now = datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S')
    sleep(1)
    return time_now


def num_elements():
    """Возвращает введенный параметр: количество элементов списка"""
    return int(input('Введите количество элементов списка: '))

lst = [time_print() for _ in range(num_elements())]
print(lst)
