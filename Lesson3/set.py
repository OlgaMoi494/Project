my_set = {'a', 1, 5, 'b', '!'}
my_set1 = set([1, 6, 7, 'h', 'H', "'"])
my_set3 = my_set.copy()
my_set3.add(8)
print(my_set3)
print(my_set.isdisjoint(my_set1)) # True if no common elements in 2 sets
my_set2 = {'a','b'}
print(my_set2.issubset(my_set)) # True if a set is a part of another set
print(my_set.issuperset(my_set2)) # Reverse of issubset
print(my_set | my_set1 | my_set3, my_set.union(my_set1, my_set3))  # union of several sets
print(my_set & my_set1 & my_set3, my_set.intersection(my_set1, my_set3))
"""returns common elements in several sets compared"""
print(my_set - my_set1 - my_set3, my_set.difference(my_set1, my_set3))
"""returns elements available in the deducted set (my_set)"""
print(my_set ^ my_set1, my_set.symmetric_difference(my_set1)) # returns elements that differ in 2 compared sets
""""For set only, modifies the set! Print separately"""
my_set.intersection_update(my_set3)
my_set &= my_set1
print(my_set)
my_set.update(my_set1)
my_set |= my_set3
print(my_set)
my_set.difference_update(my_set1)
my_set = {'a', 1, 5, 'b', '!'}
print(my_set)
'''Аналогично symmetric_difference и ^= '''
my_set.add(8) #adds element to the set
print(my_set)
my_set.remove(8) #removes element from the set, if no such element returns error
print(my_set)
my_set.discard(8) #removes element from the set if available
print(my_set)
my_set.pop() #removes arbitrary  element from the set, error if the set is empty
print(my_set)
my_set.clear() #removes all elements from the set
print(my_set)
