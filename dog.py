class Dog:
    species = 'Canis familiaris'
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return self.name

    def description(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound='Uou'):
        return super().speak(sound)

class Akita(Dog):
    pass

class Husky(Dog):
    pass


if __name__ == '__main__':
    bruce = GoldenRetriever('Bruce', 3, 'Golden Retriever')
    nina = Husky('Nina', 2, 'Husky')
    nala = Akita('Nala', 3, 'Akita')
    print(bruce.description())
    print(bruce.speak())