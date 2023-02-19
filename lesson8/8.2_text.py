"""2. Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать
файл и записать в него первые 2 строки и закрыть файл. Затем открыть файл на
редактирование и дозаписать оставшиеся 2 строки. В итоговом файле должны быть 4
строки, каждая из которых должна начинаться с новой строки."""

string_1 = input('Введите строку 1: ')
string_2 = input('Введите строку 2: ')
string_3 = input('Введите строку 3: ')
string_4 = input('Введите строку 4: ')

f = open('txt_file.txt', 'w', encoding='utf-8')
try:
    f.write(string_1)
    f.write('\n')
    f.write(string_2)
finally:
    f.close()

with open('txt_file.txt', 'a', encoding='utf-8') as f:
    f.write('\n')
    f.write(string_3)
    f.write('\n')
    f.write(string_4)

check_file = print('Проверьте файл "txt_file.txt".')