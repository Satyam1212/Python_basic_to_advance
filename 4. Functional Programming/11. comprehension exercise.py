some_list =['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates) # ['b', 'n']

# The above code can be written in a single line using list comprehension

duplicates2 = list(set([value for value in some_list if some_list.count(value) > 1]))

print(duplicates2) # ['b', 'n']