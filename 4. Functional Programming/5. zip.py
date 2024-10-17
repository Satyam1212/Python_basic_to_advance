my_list =[1,2,3]
your_list =(10,20,30)

print(list(zip(my_list, your_list))) # [(1, 10), (2, 20), (3, 30)]

your_list2 =[100,200,300]

print(list(zip(my_list, your_list, your_list2))) # [(1, 10, 100), (2, 20, 200), (3, 30, 300)]

print(list(zip(my_list, your_list2))) # [(1, 100), (2, 200), (3, 300)]

# zip is used to combine two or more lists. It will combine the lists element wise.

# we can use this in database to combine the data from different tables.