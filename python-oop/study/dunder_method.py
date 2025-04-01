class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return "{} age is {}".format(self.name, self.age)

    def __len__(self):
        return self.age

tom = Employee("Tom Lannister", 47)
print(tom)
print(len(tom))