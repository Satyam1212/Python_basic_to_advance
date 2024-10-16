# Polymorphism: Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email) # calling the parent class constructor
        # or super().__init__(email) # calling the parent class constructor
        self.power = power
        self.name = name

    def attack(self):
        User.attack(self) # calling the parent class method 
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.num_arrows = num_arrows
        self.name = name

    def attack(self):
        print(f'attacking with num_arrows of {self.num_arrows}')

wisard1 = Wizard("Ram", 40, "m@gmail.com")
archer1 = Archer("Robin", 100)

print(wisard1.attack()) # attacking with power of 40

def player_attack(char):
    char.attack()

player_attack(wisard1) # attacking with power of 40
player_attack(archer1) # attacking with num_arrows of 100

# Same function giving different outputs based on the object passed to it is called polymorphism

for char in [wisard1, archer1]:
    char.attack() # gives the same output as above

print(wisard1.email) # m@gmail.com

# Introspection: The ability to determine the type of an object at runtime

print(dir(wisard1)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attack', 'email', 'name', 'power', 'sign_in']

# we have dunder methods which are inherited from the object class