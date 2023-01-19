from timeit import timeit
# print(f"Создание кортежа: {timeit('(1,2,3,4)')}")
# print(f'''Создание строки: {timeit('"1,2,3,4"')}''')
# print(f"Создание списка: {timeit('[1,2,3,4]')}")
# print(f"Создание множества: {timeit('{1,2,3,4}')}")
# print(f'''Разбить строку на список: {timeit('"1,2,3,4".split(",")')}''')
# print(f"Сделать копию списка: {timeit('[1,2,3,4][:]')}", '\n')

print("Формирование последовательности Фибоначчи:")
print(timeit(
'''
a = 0
b = 1
lst_fib = [a,b]
for _ in range(15):
    temp = a
    a = b
    b = temp + a
    lst_fib.append(b)
'''))

