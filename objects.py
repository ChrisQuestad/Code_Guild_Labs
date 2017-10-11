# Object = Way to encapsulate data. Allows you to store data and implement functionality.
# class __dict__: Shows values as a dictionary
class Animal:
    def __init__(self, height, num_legs, skin, sound):
        self.height = height
        self.num_legs = num_legs
        self.skin = skin
        self.sound = sound

    def describe(self):
        print(f'I am a(n) {self.__class__.__name__} and have {self.num_legs} legs!')


class Dog(Animal):
    pass

class Husky(Dog):
    def describe(self):
        super().describe()
        print('AWOOOOOOOOOOOOOOO')


animal = Husky(2, 5, 'furry', 'speaks')
print(animal.__dict__)
animal.describe()
