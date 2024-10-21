print({char for char in 'hello'}) # {'e', 'l', 'o', 'h'}

# Set is similar to list but it does not allow duplicates

my_dict = { key: value ** 2 for key, value in dict(a=1, b=2, c=3, d=4).items() if value % 2 == 0}

print(my_dict) # {'a': 1, 'b': 4, 'c': 9, 'd': 16}

my_dict2 = { num: num*2 for num in [1, 2, 3]}

print(my_dict2) # {1: 2, 2: 4, 3: 6}