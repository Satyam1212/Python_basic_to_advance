# Tuple

# Tuple is a collection of immutable objects.
# Tuple is ordered.
# Tuple is indexed.
# Tuple is written with round brackets.
# Tuple can store duplicate values.
# Tuple is faster than list.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple) # (1, 2, 3, 4, 5)
print(my_tuple[2]) # 3

print(5 in my_tuple) # True

tuple_user = {
    (1, 2): [1, 2, 3],
    'name': 'John',
    'age': 25
}

print(tuple_user[(1, 2)]) # [1, 2, 3]

print(my_tuple[1:4]) # (2, 3, 4)

print(my_tuple * 2) # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

print(len(my_tuple)) # 5

print(my_tuple[1:2]) # (2,)

x,y,z, *other = my_tuple

print(x) # 1

print(my_tuple.index(3)) # 2    