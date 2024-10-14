# Everything in python is an object

# Class is a blueprint for creating objects
# Object is an instance of a class
# Class -> Instantiate -> Instances

# OOP is like paradigm to way think about code and structure code

class BigObject: # Class
    pass

print(type(BigObject)) #<class 'type'>

obj1 = BigObject() # Object(Instantiate) # We creating new object by instantiating the class

print(type(obj1)) #<class '__main__.BigObject'>

# Efficiecy
# Blueprint is class store in memory
# But every time create object we will tell python DRY(Don't Repeat Yourself) to create new object in memory and store it