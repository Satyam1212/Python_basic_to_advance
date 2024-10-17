# reduce
# The reduce function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This function is defined in “functools” module.

from functools import reduce
# functools is a module for higher-order functions and operations on callable objects.

my_list = [1,2,3]

def accumulator(acc, item):
    print(acc, item)
    return acc + item

# below 0 is the initial value of acc
print(reduce(accumulator, my_list, 0)) 
"""
answer:

0 1
1 2
3 3
6

"""