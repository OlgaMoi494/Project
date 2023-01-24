def if_isnum(input_string: str) -> None:
    '''Функция принимает на вход число в строковом формате и печатает его числовой формат, ничего не возвращает'''

    positive = True
    if input_string[0] == '-':
        str_lst = input_string[1:].split('.')
        str_lst_digit = list(filter(lambda x: x.isdigit(), str_lst))
        positive = False
    else:
        str_lst = input_string.split('.')
        str_lst_digit = list(filter(lambda x: x.isdigit(), str_lst))

    if (str_lst_digit == str_lst and len(str_lst_digit) == 2) or (len(str_lst_digit) == 1 and str_lst[0] == ''
                                                                  and '.' in input_string):
        number = float(input_string)
        if positive:
            print(f'Вы ввели положительное дробное число {number}.')
        else:
            print(f'Вы ввели отрицательное дробное число {number}.')

    elif str_lst_digit == str_lst and len(str_lst_digit) == 1:
        number = int(input_string)
        if positive:
            print(f'Вы ввели положительное целое число {number}.')
        else:
            print(f'Вы ввели отрицательное целое число {number}.')
    else:
        print(f'Вы ввели некорректное число {input_string}.')

str_ = input('Введите любое число: ').strip()
if_isnum(str_)
