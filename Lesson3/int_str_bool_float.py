text = '''
 Онлайн-курс «Интернет-маркетинг для начинающих» даёт представление о принципах работы
информационных систем, обеспечивающих решение задач интернет-маркетинга. Рассмотрены
основы продвижения продукта/услуги с использованием интернет-ресурсов.
 '''
print(text.encode())
print(text.lower().count('.')) #подсчет точек
print(text.index('.',text.index('.') + 1)) # индекс второй точки
print(text.replace('«', '\'').replace('»', '\''))
print(text[text.find('«'):text.rfind('маркетинг')+len('маркетинг')+1]) #создание среза через поиск символов
print()
text_1 = 'Hello'
text_1_lst = list(text_1)
print(f'str.join(iterable) соединяет итерабельный объект в строку {text_1_lst} => {"".join(text_1_lst)} ')
hello_centered = '"' + text_1.center(len(text_1)*3,'!') + '"' # центрирует по указанной в количестве символов ширине
print(hello_centered)
print(hello_centered.strip('!"')) #удаляет лишние знаки в начале и конце слова
text_2 = 'voLHa buiniTskAya vaLENTinovna'
print(text_2.capitalize()) # делает первую букву заглавной - остальные маленькие
print(text_2.title()) # делает первую букву каждого слова заглавными - остальные маленькие
print('Volha\tBuinitskaya\tValentinovna'.expandtabs(16)) #регулирует количество табов
print(text.partition('.')) # разбивает строку на три части по разделителю: (1-я часть, разделитель, 2-я часть)
print(text.split(),'\n') #разбивает строку в список по разделителю
text_3 = 'abcABCПривет123!@#.,'
print(f'str.isnum()  - True, если буквы и цифры, пример: ')
print(f'{text_3, text_3.isalnum()} и {text_3.strip("!@#,."), text_3.strip("!@#.,").isalnum()}.\n')
print(f'str.isalpha()  - True, если буквы, пример:')
print(f' {text_3,text_3.isalpha()} и {text_3.strip("123!@#,."),text_3.strip("123!@#,.").isalpha()}.')
print()
text_4 = '33.'
print(f'str.isdecimal()  - True, если только цифры, пример:')
print(f' {text_4,text_4.isdecimal()} и {text_4.strip("."),text_4.strip(".").isdecimal()}.')


import math
print('Welcome to integers and floats!')
number = -30
print(f'abs(x) Модуль числа {number} равно {abs(number)}.')
number_1 = 12
print(f'divmod(x, y) Целая и дробная части деления чисел  {number} и {number_1} равны {divmod(number,number_1)}.')
print(f'Результат деления "/" всегда дает float: 30 / 10 = {30 / 10}')
print(f'Результат целочисленного деления "//" всегда дает int: 30 / 12 = {30 // 12}')
print(f'Результат остатка деления "%" всегда дает int: 30 % 12 = {30 % 12}')
number_2 = 3.56
print(f'Число {number_2}, округление с заданной точностью: {round(number_2,1)}, округление вверх {math.ceil(number_2)}.')
a = float('nan')
print(f'Формат float может принимать "Nan" - Not a Number, пример: значение - {a} - {type(a)}')
print()
print('Welcome booleans!')
print(f'Значение bolean 1: {bool(1)} , 0: {bool(0)}')
print(f'Значение bolean не 1: {bool(not 1)} , не 0: {bool(not 0)}')
bool_var = True
print(f'Bool_var = True, True ==1: {bool_var == 1}, True == 2: {bool_var == 2}, bool(2): {bool(2)}.')
'''Идентификация булевых значений и чисел'''
