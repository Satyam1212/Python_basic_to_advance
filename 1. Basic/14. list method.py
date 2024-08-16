basket = [1, 2, 4,5]

# adding
new_list = basket.append(100)

print(basket) # [1, 2, 4, 5, 100]
print(new_list) # None

# To create a new list from the original list, use the following method
new_list2 = basket

print(new_list2) # [1, 2, 4, 5, 100]

# adding inserting
new_list2.insert(4, 100)

print(new_list2) # [1, 2, 4, 5, 100, 100]

# adding extending
new_list2.extend([101, 102])

# removing
new_list2.pop() # removes the last item in the list

print(new_list2) # [1, 2, 4, 5, 100, 100, 101]

new_list2.pop(0) # removes the item at index 0

# clearing

new_list2.clear()
print(new_list2) # None

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
new_basket = basket[:]
print(basket.index('d')) # 4

# print(basket.index('d', 0, 4)) # 4

print('d' in basket) # True

print('x' in 'hi my name is x') # True

# count : counts the number of times an item appears in a list
print(basket.count('d')) # 2

# sort
basket.sort()
print(basket) # ['a', 'b', 'c', 'd', 'd', 'e', 'x']

basket.sort(reverse=True)
print(basket) # ['x', 'e', 'd', 'd', 'c', 'b', 'a']

print(sorted(basket)) # ['a', 'b', 'c', 'd', 'd', 'e', 'x']
print(new_basket)

print(range(1, 100)) # range(1, 100)

print(list(range(1, 100)))

print(list(range(101)))

sentence = '!'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Jojo'])
print(new_sentence) # hi!my!name!is!Jojo

# list unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a) # 1
print(b) # 2
print(c) # 3
print(other) # [4, 5, 6, 7, 8]

a = None
print(a) # None