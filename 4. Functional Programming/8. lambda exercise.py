my_list = [5, 4, 3]

print(list(map(lambda i: i **2, my_list))) # [25, 16, 9]

print(list(filter(lambda i: i % 2 != 0, my_list))) # [5, 3]

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(a.sort()) # None
a.sort(key=lambda x: x[1])
print(a) # [(10, -1), (0, 2), (4, 3), (9, 9)]