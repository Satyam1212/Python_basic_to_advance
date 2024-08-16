#booleans

#Booleans represent one of two values: True or False.

from datetime import datetime


name = 'Satyam'
is_cool = False

is_cool = True

print(bool(0)) #False
print(bool(1)) #True


birth_year = input('What year were you born?')

age = datetime.today().year - int(birth_year)

print(f'Your age is: {age}')


"""
Exercise:
"""

username = input('Enter your username: ')
password = input('Enter your password: ')

print(f"{username}, password {'*'*len(password)} is {len(password)} letters long")