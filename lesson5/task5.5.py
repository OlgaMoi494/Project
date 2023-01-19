from random import randint
from replit import clear
while True:
    answer = randint(1, 10)
    print('Угадай число от 1 до 10!')
    guess = 0
    while guess != answer:
        guess = int(input('Введи число: '))
        if guess < answer:
            print('Введенное число слишком маленькое.')
        elif guess > answer:
            print('Введенное число слишком большое.')
    else:
        print(f'Ты угадал, это число {answer}!')

    if input('Хочешь сыграть еще раз? "да" или "нет": ').lower() in ('нет', 'н'):
        break
    else:
        clear() #почему то clear не работает
