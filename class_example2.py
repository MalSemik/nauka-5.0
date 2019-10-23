class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('Miau')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('Hau')


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('Muuu')


animals = [Cat('Puszek'), Dog('Borys'), Cow('Balbinka')]
for animal in animals:
    animal.speak()

