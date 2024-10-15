# 4 Pillars of OOP

# Encapsulation
# Binding the data(attributes) and methods(functions) that manipulate the data into a single unit

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('andrei', 10)
player1.speak() # my name is andrei, and I am 10 years old


player2 = {'name': 'jill', 'age': 10}
player2['name'] # jill
player2['age'] # 10

# Both are doing the same thing but the first one is more organized and easy to understand and maintain than the second one