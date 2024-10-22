# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
# DEcorators are used to modify the behavior of functions or methods.
# They are looks like @classmethod, @staticmethod, @property, @abstractmethod etc.

# In python functions are first class objects, which means that they can be passed around like variables.

# Example 1:

def hello():
    return 'Hello!'

greet = hello
# del hello
# hello() # NameError: name 'hello' is not defined

print(greet()) # Hello!

# Example 2:

def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func

@my_decorator
def sim():
    print('This is a simple function!')

sim() # ********
        # This is a simple function!
        # ********

@my_decorator
def greet():
    print('Hello!')

greet() # ********
        # Hello!
        # ********

# Example 3: with arguments

def my_decorator(func):
    def wrap_func(x):
        print('********')
        func(x)
        print('********')
    return wrap_func

@my_decorator
def greet(name):
    print(f'Hello {name}!')

greet('World') # ********
                # Hello World!
                # ********

# Example 4: with multiple arguments

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('********')
    return wrap_func

@my_decorator
def greet(name, emoji):
    print(f'Hello {name} {emoji}!')

greet('World', ':)') # ********
                        # Hello World :)
                        # ********

@my_decorator
def greet(name, emoji=':()'):
    print(f'Hello {name} {emoji}!')

greet('World') # ********
                # Hello World :)
                # ********
