number = int(input('Введите целое число: '))

if_even = lambda x: 'четное' if x % 2 == 0 else 'нечетное'

print(f'Введенное число {number} - {if_even(number)}')
