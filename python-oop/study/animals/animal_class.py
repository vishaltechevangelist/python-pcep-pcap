class Animal:
    def __init__(self, name):
        self.animal_name = name

    def eat(self):
        raise NotImplementedError("Child class should be implementing this")


class Monkey(Animal):
    def eat(self):
        print("Monkey eating banana")


class Bird(Animal):
    def eat(self):
        print("Bird eating insect")

    def fly(self):
        print("Bird soaring high")

mydog = Monkey('Tommy')
mydog.eat()

mybird = Bird("Tom")
mybird.fly()