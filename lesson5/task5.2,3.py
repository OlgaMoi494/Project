while True:
    name = input('Введите имя: ').capitalize()
    age = input('Введите возраст: ')

    while age.isdecimal() == False or int(age) <= 0:
        age = input('Ошибка, повторите ввод: ')

    age = int(age)
    if age < 10:
        print(f'Привет, шкет {name}')
    elif 10 <= age <= 18:
        print(f'Как жизнь, {name}?')
    elif 18 < age < 100:
        print(f'Что желаете, {name}?')
    else:
        print(f'{name}, вы лжете - в наше время столько не живут...')
