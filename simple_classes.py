import re

cities = list()     #  list cities = new list();

x = 5    #   int x = new int(5)       x = int(5)

print(f"type(cities): {type(cities)}")
print(f"type(x): {type(x)}")
print(f"type(re): {type(re)}")

t = type(cities)

colors = t()
print(f"colors: {colors}")
print(f"type(colors): {type(colors)}")

class Animal:  # inherits from 'object' -- provides default __str__() and __init__()
    def __init__(self):
        print("building an animal")

    def run(self):   # 'self' == 'this'
        print("running...")

class Pet:
    pass

class Dog(Animal, Pet):    # super().__init__()  Animal.__init__()
    def bark(self):
        print("Woof! woof!")

d1 = Dog()
d2 = Dog()
d2.bark()
d1.run()
print(f"Dog.mro(): {Dog.mro()}")




