"""5. Прочитать сохранённый csv-файл и сохранить данные в excel-файл, кроме возраста - столбец с этими данными
не нужен."""

import csv
import openpyxl

with open('csv_file.csv', newline='') as src_file:
    file_reader = csv.reader(src_file)
    data = list(file_reader)  # читаем файл в формате списка

pop_age = [i.pop(2) for i in data]  # удаляем возвраст

persons = []
for i in range(1, len(data)):
    persons.append('person ' + str(i))  # формируем список заголовков для эксель

book = openpyxl.Workbook()  # создаем файл эксель
sheet = book.active

for column in range(2, len(persons) + 2):
    sheet.cell(1, column).value = persons[column - 2]  # записываем заголовки в эксель

for row in range(2, len(data[0]) + 2):
    for column in range(1, len(data) + 1):
        sheet.cell(row, column).value = data[column - 1][row - 2]  # записываем данные в эксель

book.save('csv_to_excel.xlsx')
book.close()

check_file = print('Проверьте файл "csv_to_excel.xlsx".')
