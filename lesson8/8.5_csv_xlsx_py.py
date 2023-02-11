"""5. Прочитать сохранённый csv-файл и сохранить данные в excel-файл,
кроме возраста - столбец с этими данными не нужен."""

import csv
import openpyxl

with open('csv_file.csv', newline='') as src_file:
    file_reader = csv.reader(src_file)
    data = list(file_reader)  # читаем файл в формате списка

persons = []
for i in range(len(data)):
    if i == 0:
        persons.append(None)
    else:
        persons.append('person ' + str(i))
# формируем список заголовков для эксель

data_flip = []
for i in range(len(data[0])):
    inner_lst = []
    if i == 2:
        continue
    for j in range(len(data)):
        inner_lst.append(data[j][i])
    data_flip.append(inner_lst)
data_flip.insert(0, persons)

book = openpyxl.Workbook()  # создаем файл эксель
sheet = book.active

for item in data_flip:
    sheet.append(item)

book.save('csv_to_excel.xlsx')
book.close()

print('Проверьте файл "csv_to_excel.xlsx".')
