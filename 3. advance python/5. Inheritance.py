# Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

class User:
    def sign_in(self):
        print('logged in')

class Wizard(User): 
    def __init__(self, name, power):
        self.power = power
        self.name = name

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer():
    def __init__(self, name, num_arrows):
        self.num_arrows = num_arrows
        self.name = name

    def attack(self):
        print(f'attacking with num_arrows of {self.num_arrows}')

whizard1 = Wizard("Ram", 40)
archer1 = Archer("Robin", 100)

print(whizard1.sign_in()) # logged in
print(whizard1.attack()) # attacking with power of 40
print(archer1.attack()) # attacking with num_arrows of 100
