range(100)

list(range(100))

def make_list(num):
    return [i*2 for i in range(num)]

my_list = make_list(100)

print(my_list)

# make_list is live in memory but my_list is pointing to the list created by make_list

# range is generator  - it is not storing the list in memory but it is generating the list on the fly

# Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly:

# Everything is generators is iterable but not everything that is iterable is a generator

# e.g. range is a generator but list is not a generator

def generator_function(num):
    for i in range(num):
        yield i*2
# yield is a keyword that is used like return, except the function will return a generator

for item in generator_function(1000):
    print(item)

# Generators are best for calculating large sets of results (particularly in calculations that involve loops themselves) where you don’t want to allocate the memory for all results at the same time.

g = generator_function(1000)
print(g) # <generator object generator_function at 0x000001D3D3A3A1C8>

print(next(g)) # 0
print(next(g)) # 2

g2= generator_function(1)
print(next(g2)) # 0
# print(next(g2)) # StopIteration