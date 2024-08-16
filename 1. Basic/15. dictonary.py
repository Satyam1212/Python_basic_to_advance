# Dictonary
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

dictionary = {
    'a': 1,
    'b': 2
}

print(dictionary) # {'a': 1, 'b': 2}

print(dictionary['a']) # 1

# Dictionary are mutable

my_dict = {
    'a' : [1, 2, 3],
    'b' : 'hello',
    'c' : True
}

print(my_dict['a'][2]) # 3

my_list = [
    {
        'a' : [1, 2, 3],
        'b' : 'hello',
        'c' : True
    },
    {
        'a' : [4, 5, 6],
        'b' : 'world',
        'c' : False
    }

]
print(my_list[0]['a'][2]) # 3

# my_dict2 = {
#     123: [1, 2, 3],
#     456: 'hello',
#     [100]: True
# }

# print(my_dict2) # TypeError: unhashable type: 'list'

my_dict3 = {
    '123': [1, 2, 3],
    '123': 'hello',
    '123': True
}

print(my_dict3) # {'123': True}

"""
String is immutable. So, if we use the same key multiple times, the last value will be stored in the dictionary. 

If we use a list as a key, it will throw an error because list is mutable and it can't be hashed.

If we use a tuple as a key, it will work because tuple is immutable and it can be hashed.

If we use a string as a key, it will work because string is immutable and it can be hashed.

We use dictonary to save memory. If we have a large data and we want to access it quickly, we can use dictonary. and we could not use list because it will take more memory and time to access the data.
"""

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print(user.get('age', 55)) # 20 if age is present in the dictionary, otherwise 55

user2 = dict(name='John') # {'name': 'John'} this will give error as keywords not the expression
print(user2) # {'name': 'John'}

print('basket' in user) # True

# ITEMS
print(user.items()) # dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)]) it will return a list of tuples

# KEYS
print(user.keys()) # dict_keys(['basket', 'greet', 'age']) it will return a list of keys

# cLEAR AND COPY
USER3 = user.copy()
user4 = user.copy()
user.clear()
print(user) # {}
print(USER3) # {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}

# POP
print(USER3.pop('age')) # 20

print(USER3) # {'basket': [1, 2, 3], 'greet': 'hello'}

# POPITEMS
# It will remove the last item from the dictionary


print(user4.update({'age': 55})) # None

print(user4)