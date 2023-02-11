"""2. Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
Создатьфайл и записать в него первые 2 строки и закрыть файл. Затем открыть
файл на редактирование и дозаписать оставшиеся 2 строки. В итоговом файле
должны быть 4 строки, каждая из которых должна начинаться с новой строки."""

string_1 = input('Введите строку 1: ')
string_2 = input('Введите строку 2: ')
string_3 = input('Введите строку 3: ')
string_4 = input('Введите строку 4: ')

file = open('txt_file.txt', 'w', encoding='utf-8')
try:
    file.write(string_1)
    file.write('\n')
    file.write(string_2)
finally:
    file.close()

with open('txt_file.txt', 'a', encoding='utf-8') as file:
    file.write('\n')
    file.write(string_3)
    file.write('\n')
    file.write(string_4)

print('Проверьте файл "txt_file.txt".')
