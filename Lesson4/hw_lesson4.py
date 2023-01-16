'''Task 1:'''
var_1, var_2, var_3 = 7, 7, 7
print(id(var_1), id(var_2), id(var_3), '\n')

'Task 2:'
var_3 = [1, 2, 'a', 'b']
var_4 = [1, 2, 'a', 'b']
print(id(var_3), id(var_4), '\n')

'''Task 3:'''
var_1 = str(var_1)
var_2 = float(var_2)
print(id(var_1), id(var_2), id(var_3), '\n')

import sys
var_3 = sys.intern(''.join([str(i) for i in var_3]))
var_4 = sys.intern(''.join([str(i) for i in var_4]))    # TODO почитать статью https://habr.com/ru/post/564804/

print(id(var_3), id(var_4), '\n')

'''Task 4'''
input_str = input('Введите строку: ').strip()

lst_1 = []
lst_2 = []
for i in range(
        len(input_str)):           # TODO Николай, как можно перебрать строку без циклов? Мы циклы еще не проходили.
    if (i + 1) % 2 == 0:
        lst_1.append(input_str[i])
    else:
        lst_2.append(input_str[i])

str_1 = ''.join(lst_1)
str_2 = ''.join(lst_2)

print(f'Введена строка "{input_str}".', '\n\n')

print(str_1, str_2, sep=' ' * 5, end='!!!\n')

'''Task 5'''

int_1 = int(input('Введите первое целое число: '))
int_2 = int(input('Введите второе целое число: '))

if int_1 == int_2:
    print('Числа равны.\n')
elif int_1 > int_2:
    print('Первое число больше второго.\n')
else:
    print('Отработала секция else.\n')

'''Task 6'''

int_3 = int(input('Введите первое целое число: '))
int_4 = int(input('Введите второе целое число: '))

if int_3 > 10 and int_4 > 10:
    print('Оба числа больше 10.')
elif int_3 > 10 or int_4 > 10:
    print('Одно из чисел больше 10.')
elif not bool(int_3) is False:                      # если равно True
    print('Условие с помощью преобразования типов.')