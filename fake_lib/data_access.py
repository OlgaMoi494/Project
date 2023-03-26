def read_surnames():
    with open('surnames.txt') as surnames_file:
        lst_of_surnames = []
        for line in surnames_file:
            lst_of_surnames.append(line.split(' ')[1].strip())
        return lst_of_surnames


def read_names():
    with open("names.txt", encoding="utf-8") as names_file:
        lst_of_names = []
        for index, line in enumerate(names_file):
            if index % 2 == 0:
                blank_index = line.find(" ")
                lst_of_names.append(line[:blank_index])
    with open('surnames.txt') as surnames_file:
        for line in surnames_file:
            lst_of_names.append(line.split(' ')[0].strip())
        return lst_of_names
