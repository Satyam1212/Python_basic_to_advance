# set
# are unordered collection of unique elements

my_set = {1, 2, 3, 4, 5}
print(my_set) # {1, 2, 3, 4, 5}

my_set = {1, 2, 3, 4, 5, 5}

print(my_set) # {1, 2, 3, 4, 5}

my_set.add(6)
my_set.add(2)

print(my_set) # {1, 2, 3, 4, 5, 6}

# list to set

my_list = ['apple', 'banana', 'cherry', 'apple', 'cherry']

my_set2 = set(my_list)

print(my_set2) # {'banana', 'apple', 'cherry'}

# Set object doesn't support indexing
# print(my_set[1]) # TypeError: 'set' object is not subscriptable

# Set object doesn't support slicing
# print(my_set[1:3]) # TypeError: 'set' object is not subscriptable

# we can convert set to list

# Methods

my_set3 = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8}

#.diffrence() # returns a set containing the difference between two or more sets
print(my_set3.difference(your_set)) # {1, 2, 3}

print(my_set3.discard(5)) # None
print(my_set3) # {1, 2, 3, 4}

print(my_set3.difference_update(your_set)) # None
print(my_set3) # {1, 2, 3}

my_set3.add(4)

print(my_set3.intersection(your_set)) # {4}

print(my_set3.isdisjoint(your_set)) # False # if two sets have a null intersection

print(my_set3.union(your_set)) # {1, 2, 3, 4, 5, 6, 7, 8}

print(my_set3.issubset(your_set)) # False

print(my_set3.issuperset(your_set)) # False

print(my_set3.symmetric_difference(your_set)) # {1, 2, 3, 5, 6, 7, 8}

print(my_set3.update(your_set)) # None

print(my_set3) # {1, 2, 3, 4, 5, 6, 7, 8}
