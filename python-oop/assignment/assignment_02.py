# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""
# Your Code Below:

class Animals:
    def __init__(self):
        print("Animal constructed")

    def move(self):
        print("Animal is moving")

    def eat(self):
        print("Animal is eating")

class Bird(Animals):
    def __init__(self, bird_age, bird_name):
        #Animals.__init__(self)
        self.name = bird_name
        self.age = bird_age

    def move(self):
        print("The {} is flying".format(self.name))

class Dog(Animals):
    def __init__(self, dog_age, dog_name):
        Animals.__init__(self)
        self.name = dog_name
        self.age = dog_age

    def move(self):
        print("The dog is running")

class Fish(Animals):
    def __init__(self, fish_age, fish_name):
        Animals.__init__(self)
        self.name = fish_name
        self.age = fish_age

    def move(self):
        print("The fish is swimming")

bird = Bird("Parrot", 15)
# dog = Dog("Tom", 15)
# fish = Fish("Neo", 1)
#
bird.move()
# dog.move()
# fish.move()

bird.eat()
# dog.eat()
# fish.eat()













































# Solution:
# class Animal:
#     def __init__(self):
#         print("Animal Constructed")
#
#     def move(self):
#         print("Animal Moving...")
#
#     def eat(self):
#         print("Animal Eating...")
#
#
#
# class Bird(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Bird flying...")
#
#
#
# class Fish(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Fish Swimming...")
#
#
# class Dog(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Dog Running ...")
#
# mydog = Dog(3, "wolfy")
# mydog.move()
# mydog.eat()
#
# mydog = Fish(1, "nemo")
# mydog.move()
# mydog.eat()
#
# mydog = Bird(3, "jojo")
# mydog.move()
# mydog.eat()