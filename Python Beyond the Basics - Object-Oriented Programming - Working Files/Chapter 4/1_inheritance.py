# Example 1
class Date(object):
    def get_date(self):
        return "2018-5-25"

class Time(Date):
    def get_time(self):
        return "16:21:00"

dt = Date()
print(dt.get_date())

tm = Time()
print(tm.get_time())
print(tm.get_date())

# Example 2
class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print("{} is eating {}.".format(self.name, food))

class Dog(Animal):
    def fetch(self, thing):
        print("{} goes after the {}".format(self.name, thing))

class Cat(Animal):
    def swatstring(self):
        print("{} shreds the string!".format(self.name))

r = Dog("Rover")
f = Cat("Fluffy")

r.fetch("paper")
f.swatstring()
r.eat("Dog Food")
f.eat("Cat food")