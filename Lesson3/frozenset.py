my_frozen_set = frozenset(['s', 1, 'df', 33, 'H', '!'])
my_dict = {}
my_dict[my_frozen_set] = 1  # frozenset can be key in the dictionary
print(my_dict)
my_set = {1, 2, 'a'}
my_set.add(8)
my_set.add(my_frozen_set)  # frozenset can be an element of a set
print(my_set)
my_new_frozen_set = my_frozen_set.union(my_set)
print(my_new_frozen_set)
