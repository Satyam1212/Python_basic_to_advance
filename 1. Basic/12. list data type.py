# List data type
# Definition: A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

# List are mutable

li = [1,2,3,4,5]

li2 = ['a', 'b', 'c']

li3 = [1,2,3,4,5,'a', 'b', 'c']
print(li, li2, li3)

# Data Structure
# A particular way of organizing data in a computer so that it can be used effectively.

# List Slicing

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

print(amazon_cart[0:2]) # ['notebooks', 'sunglasses']

print(amazon_cart[0::2]) # ['notebooks', 'toys']

amazon_cart[0] = 'laptop'

new_cart = amazon_cart # This will create a reference to the original list and not a new list

# To create a new list from the original list, use the following method
new_cart = amazon_cart[:] # This will create a new list from the original list

new_cart[0] = 'gum'
print(new_cart) # ['gum', 'sunglasses', 'toys', 'grapes']
print(amazon_cart) # ['gum', 'sunglasses', 'toys', 'grapes']