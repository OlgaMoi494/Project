'''ЗАДАНИЕ 4
Написать функцию, которая принимает n-ое количество координат точек.
И в ответ возвращает длину маршрута между ними.
Каждая координата представлена кортежем, состоящим из двух объектов типа int.
Длина отрезка: https://www.calc.ru/Formula-Dliny-Otrezka.html
Примеры использования функции:
result = distance((1, 1), (1, 2), (3, 3))
print(result) # выведет 1
'''


def distance(*args: tuple) -> float:
    '''Returns distance among sequence of points of coordinates'''
    distance_length = 0
    for item in range(len(args) - 1):
        vector_length = ((args[item + 1][0] - args[item][0]) ** 2 + (
                    args[item + 1][1] - args[item][1]) ** 2) ** 0.5
        distance_length += vector_length
    return distance_length


result = distance((1, 1), (1, 2), (3, 3))

print(f'Длина маршрута между заданными точками составляет {round(result, 2)}')
