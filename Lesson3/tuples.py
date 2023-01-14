empty_tuple = ()
one_element_tuple = ('Element',)  # add a comma at the end
one_more_tuple = 'A', 'b', 'c'
a1, a2, a3 = one_more_tuple  # unpacking the tuple
print(a1, a2, a3)
new_combined_tuple = one_element_tuple + one_more_tuple  # adding tuples
print(new_combined_tuple)
print()

my_tuple = (1, 2, 3, [2, 3])  # tuple element can be mutable
print(my_tuple[3])
new_dct = {"c": "2"}
my_tuple[3][0] = new_dct
print(my_tuple)
