# Strings in Python are immutable i.e. they cannot be changed

selfish = '01234567'

selfish[0] = '5' #TypeError: 'str' object does not support item assignment
# So you cant reassign part of the string

# Only way to change this is complete change the string like
# selfish = '8'

print(selfish)