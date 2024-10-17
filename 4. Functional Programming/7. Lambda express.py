# lambda expressions
# lambda expressions are small anonymous functions
# they can have any number of arguments, but can have only one expression

# lambda param: action(param)

my_list = [1,2,3]

print(list(map(lambda item: item*2, my_list))) # [2, 4, 6]

print(list(filter(lambda item: item % 2 != 0, my_list))) # [1, 3]