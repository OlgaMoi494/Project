my_lst = [1, 5, 4, "h", 'A', ['a', 'g']]
my_lst1 = my_lst.copy()  # shallow copy if no nested data are to be changed
my_lst[0] = 200
print(my_lst)
print(my_lst1, '\n')
my_lst2 = my_lst[:]  # shallow copy if no nested data are to be changed

import copy

my_lst1 = copy.deepcopy(my_lst)  # deepcopy if nested data structure are to be changed
index_required = my_lst.index(['a', 'g'])  # finding out index position from a value given
my_lst[index_required][0] = 100
print(my_lst)
print(my_lst1, '\n')

print(my_lst[::-1], '\n')  # reverse sorting

my_lst.append('Olga')  # adding element
print(my_lst)
my_lst.insert(0, 'new')  # inserting element into a certain place
print(my_lst)
print(my_lst * 3)  # extend list by multipliying data
my_lst3 = ['I', 'would', 'like', 'to', 'see']
my_lst.extend(my_lst3)
print(my_lst)
my_lst4 = ['some', 'more']
print(my_lst + my_lst4)
my_lst[:3] = [1, 2, 10]  # changing the while slice of the list
print(my_lst)
del my_lst[:3]  # delete elements
print(my_lst)
deleted_item = my_lst.pop(0)  # to get and delete the item on the position
print(deleted_item, my_lst)
print(my_lst.count('h'))  # counting a given value in the list
my_lst.remove([100, 'g'])  # delete elements on the value
print(my_lst)
my_lst5 = sorted(my_lst)  # returns  a copy of the sorted list
my_lst.sort(reverse=True)  # alters the list
print(my_lst5)
print(my_lst)
zip_lst1 = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
zip_lst2 = ['sleep', 'snore', 'idle', 'wallow']
zip_lst3 = [1, 2, 3, 4]
print(list(zip(zip_lst1, zip_lst2, zip_lst3)))  # makes list of tuples combined of list values
print(dict(zip(zip_lst1, zip_lst2)))  # make a dict made of values of 2 lists
print(tuple(zip(zip_lst1, zip_lst2)))  # make a tuple of tuples made of values of 2 lists
my_lst6 = [1, 2, 3]
a, b, c = my_lst6  # unpacking the list
print(a, b, c)
my_lst.clear()
