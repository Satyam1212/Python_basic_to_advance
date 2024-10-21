# list, set, dictionary comprehensions

# List Comprehensions
# list = [param for param in iterable]
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list) # ['h', 'e', 'l', 'l', 'o']

# The above code can be written in a single line using list comprehension

my_list = [char for char in 'hello']

print(my_list) # ['h', 'e', 'l', 'l', 'o']

print([num for num in range(0, 100)])

print([num ** 2 for num in range(0, 100)])

print([num ** 2 for num in range(0, 100) if num % 2 == 0])