for item in (1, 2, 3, 4):
    print(item) # 1 2 3 4
    for char in 'hello':
        print(char) # h e l l o
    for i in range(2):
        print(i) # 0 1
    for x in [1, 2, 3]:
        print(x) # 1 2 3

user = {
    'name': 'John',
    'age': 25,
    'is_verified': True
}

for key in user:
    print(key) # name age is_verified

for item in user.items():
    print(item) # ('name', 'John') ('age', 25) ('is_verified', True)

for key, value in user.items():
    print(key, value) # name John age 25 is_verified True

for value in user.values():
    print(value) # John 25 True


# for i in 50:
#     print(i) # TypeError: 'int' object is not iterable

# Exercise

# counter

my_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counter = 0
for i in my_count:
    counter += i
    
print(counter)

for _ in range(10):
    print('Hello') # 10 times Hello

for _ in range(0,10,2):
    print('Hello') # 5 times Hello

for _ in range(10, 0, -1):
    print(_) # 10 9 8 7 6 5 4 3 2 1

for _ in range (10, 0):
    print(_) # nothing

for _ in range(2):
    print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for char in enumerate('hello'):
    print(char) # (0, 'h') (1, 'e') (2, 'l') (3, 'l') (4, 'o')

for i, char in enumerate((1, 2, 3, 4)):
    print(i, char) # 0 1 1 2 2 3 3 4

for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print(f'Index of 50 is {i}') # Index of 50 is 50


# while loop
while True:
    response = input('Say something: ')
    if response == 'bye':
        break

# break - exits the current loop
# continue - skips the current iteration and goes to the next iteration

for item in [1, 2, 3, 4, 5]:
    if item == 3:
        continue
    print(item) # 1 2 4 5

# pass - does nothing
for item in [1, 2, 3, 4, 5]:
    pass
    print(item) # 1 2 3 4 5