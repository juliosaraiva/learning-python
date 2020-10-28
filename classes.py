class User:
    def sign_in(self):
        print('Logged in')


class Character:
    def attack(self):
        pass


class Wizard(User, Character):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User, Character):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        self.arrows -= 1
        print(f'{self.name} Attacking... there are {self.arrows} available')


wizard = Wizard('Dark Magician', 100)
wizard.attack()
archer = Archer('Robin Wood', 150)
archer.attack()
archer.attack()
archer.attack()
archer.attack()
archer.attack()
archer.attack()
archer.attack()
archer.attack()
archer.attack()
archer.attack()
archer.attack()
archer.attack()