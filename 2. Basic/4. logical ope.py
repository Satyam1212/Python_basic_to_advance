# Logical Operators
# Logical operators are the and, or, not operators.

# ==, !=, >, <, >=, <= are comparison operators.

print(10 > 9 and 10 < 20)  # True

print('a' > 'b') # False
# 'a' is 97 and 'b' is 98 in ASCII

print('a' > 'A') # True
# 'a' is 97 and 'A' is 65 in ASCII

print(not 10 > 9) # False

print(True == 1) # True
print(False == 0) # True
print('' == 1) # False
print('1' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([] == []) # True


# is vs ==
# is is used to compare the memory location of two objects. == is used to compare the values of two objects.

print(True is 1) # False
print(True == 1) # True
print([] is []) # False
print([] == []) # True
print('1' is 1) # False
print('1' == 1) # False
print(10 is 10.0) # False
print(10 == 10.0) # True
print('hello' is 'hello') # True
print('hello' == 'hello') # True

print([1, 2, 3] is [1, 2, 3]) # False
print([1, 2, 3] == [1, 2, 3]) # True

# Data strutures created in different memory locations. So, is operator returns False. But, the values are same. So, == operator returns True.