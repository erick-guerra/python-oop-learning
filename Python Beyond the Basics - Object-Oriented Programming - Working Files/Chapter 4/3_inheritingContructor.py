import random

class Animal(object):
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    """ We call the parent class constructor with super. Super is a built in function and its designed
     to relate a class to its super class (parent class). In this example we are saying... Get the superclass of dog
     and pass dog to what ever instance we say in the constructor. Super is best use practice, instead of calling
     'Animal.__init__', doing so allows use to keep modular and easy to maintain and change """
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Poodle', 'Boxer', 'Mutt'])

    def fetch(self, thing):
        print("{}, of the {} breed,  goes after the {}".format(self.name, self.breed, thing))

d = Dog("Rover")
print(d.name)
print(d.breed)
print(d.fetch("Bone"))