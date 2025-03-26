# Looping dictionaries
employees = {"Vishal": 200000, 'Priyanka': 20000, 'Dinesh': 50000}
for person in employees.items():
    print(person) # Print tuple have key & value

for person in employees.values():
    print(person) # Print values only

for person in employees.keys():
    print(person) # Print keys only

for (person, salary) in employees.items():
    print("The salary of {} is {}".format(person, salary))

employees = [("Vishal", 200000), ('Priyanka', 20000), ('Dinesh', 50000)]
for (k, v) in employees:
    print("The salary of {} is {}".format(k, v))

employees = [("Vishal", 200000, 42), ('Priyanka', 20000, 37), ('Dinesh', 50000, 70)]
for (name, salary, age) in employees:
    print("The salary of {} is {} and age is {} ".format(name, salary, age))