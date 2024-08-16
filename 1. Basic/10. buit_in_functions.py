print(len('ssssdasdcvfs'))

print('ssssdasdcvfs'.upper())

# print is a function
# upper is a method
# len is a function
"""
Definition: A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

Definition: A method in python is somewhat similar to a function, except it is associated with object/classes. Methods in python are very similar to functions except for two major differences.

find() is a method

Q. find() is also require parameter? then how it is a method?

A. Yes, find() method requires at least one parameter to work. 
But it is a method because it is associated with object/classes. which object? string object
"""

quote = 'to be or not to be'

print(quote.find('be')) #3 Means it found the first occurance of 'be' in the string

print(quote.replace('be', 'me')) #to me or not to me

print(quote) #to be or not to be

# Sting are immutable so it will not change the original string, we can overwrite it