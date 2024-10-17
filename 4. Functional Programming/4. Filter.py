"""
map vs filter
map: map is used to apply a function to all the items in an input_list.
filter: filter is used to apply a function to all the items in an input_list that satisfies a condition.

Syntax:
filter(function, list)
function: function that tests if elements of an iterable return true or false
If None, it simply returns the elements of the iterable that are true


"""

my_list = [1,2,3,4,5,6,7,8,9]

def check_odd(item):
    return item % 2 != 0

print(list(map(check_odd, my_list))) # [True, False, True, False, True, False, True, False, True]

print(list(filter(check_odd, my_list))) # [1, 3, 5, 7, 9]

print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]