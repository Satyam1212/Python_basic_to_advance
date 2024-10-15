# Abstraction is the concept of hiding the real implementation of an application from the user and emphasizing only on usage part of it.

class Abstraction:
    def __init__(self): # Dunder method
        self.__x = 1
        self.y = 2

    def display(self):
        print(self.__x, self.y)

obj = Abstraction()
obj.display() # 1 2
# so we cant know display() is implemented