# OOP
class PlayerCharacter:
    membership = True # Class Object Attribute
    def __init__(self, name, age): # Constructor
        if PlayerCharacter.membership: # or self.membership
            self.name = name # self refers to the class itself #attribute
            self.age = age #attribute

    def run(self): # If function is not returning anything then it will return None 
        print('run')
        print(f'{self.name}') # We can't do PlayerCharacter.name because name is not Class Object attribute

    @classmethod # Decorator to access class object attribute and methods without creating object
    def adding_things(cls, num1, num2):
        return cls('andy', num1 + num2)
    
    @staticmethod # Decorator to access class object attribute and methods without creating object
    def adding_things2(num1, num2):
        return num1 + num2

pl = PlayerCharacter('Cindy', 10)

print(pl.run()) # run Cindy None
player1 = PlayerCharacter('Cindy', 10)
player1.attack = 50
player2 = PlayerCharacter('Tom', 20)
print(player1.name) # Cindy
print(player1.attack) # 50
print(player1.membership) # True
print(player2.membership) # True

print(PlayerCharacter.adding_things(2, 3)) # <__main__.PlayerCharacter object at 0x000001C4C555A990>
print(player1.adding_things(2, 3)) # <__main__.PlayerCharacter object at 0x000001C4C555A990>

player4 = PlayerCharacter.adding_things(2, 3)

print(player4.age) # 5