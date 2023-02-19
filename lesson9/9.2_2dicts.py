'''ЗАДАНИЕ 2
Есть 2 словаря
first_dict = { 'a': 1, 'b': 2, 'c': 3}
second_dict = { 'c': 3, 'd': 4,'e': 5}
Необходимо их объединить по ключам, а значения ключей поместить в список,
если у одного словаря есть ключ "а", а у другого нету, то поставить значение
None на соответствующую позицию(1-я позиция для 1-ого словаря, вторая для
2-ого) merged_dict = {'a': [1, None], 'b': [2, None], 'c': [3, 3],
'd': [None, 4],'e': [None, 5]}'''

first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'c': 3, 'd': 4, 'e': 5}
join_dicts = first_dict | second_dict
keys_set = set(join_dicts.keys())

merged_dict = {}
for key in keys_set:
    lst_elem1 = first_dict.setdefault(key, None)
    lst_elem2 = second_dict.setdefault(key, None)
    merged_dict[key] = [lst_elem1, lst_elem2]
merged_dict = dict(sorted(merged_dict.items()))

print(merged_dict)
