class User():
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.power = power
        self.name = name

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.num_arrows = num_arrows
        self.name = name

    def attack_speed(self):
        print(f'attacking with num_arrows of {self.num_arrows}')

    def run(self):
        print('run')

class HybridBorg(Wizard, Archer):
    pass

hb1 = HybridBorg('Borgie', 50) # we need to pass the name and power as the Wizard class is the first class in the HybridBorg class

print(hb1.sign_in()) # logged in
print(hb1.attack_speed()) # here it will give an error as the attack_speed method is not present in the Wizard class and the Archer class is the second class in the HybridBorg class
print(hb1.run()) # run

# To work

class HybridBorg2(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)

hb2 = HybridBorg2('Borgie', 50, 100)

print(hb2.sign_in()) # logged in
print(hb2.attack_speed()) # attacking with num_arrows of 100
print(hb2.run()) # run
print(hb2.attack()) # attacking with power of 50
