from datetime import datetime
from functools import reduce

def time_writer(func):
    '''Рассчитывает время выполнения основной функции'''
    def wrap(*args, **kwargs):
        start_time = datetime.now()
        print(f'Время старта: {start_time}')
        print(func(*args, **kwargs))
        end_time = datetime.now()
        print(f'Время старта: {end_time}')
        print(f'Время выполнения функции: {end_time - start_time}')
    return wrap

@time_writer
def add_sum_factorial(n: int) -> int:
    'Складывает сумму и факториал последовательностей заданного порядка n и возвращает результат.'
    lst = [i for i in range(1, n + 1)]
    lst_sum = reduce(lambda x, y: x + y, lst)
    lst_factorial = reduce(lambda x, y: x * y, lst)
    print('Результат вычисления: ')
    return lst_sum + lst_factorial

add_sum_factorial(1000)
print()

@time_writer
def fibonacci(n: int) -> list:
    '''Возвращает список последовательности Фибоначчи заданного порядка n.'''
    a = 0
    b = 1
    lst_fib = [a, b]
    for _ in range(n):
        temp = a
        a = b
        b = temp + a
        lst_fib.append(b)
    print('Последовательность Фибоначчи: ')
    return lst_fib

fibonacci(200)
