animal = 'Gorilla'

if animal == 'Cow':
    print("It eats grass")
elif animal == 'Bird':
    print("It eats insect and seed")
elif animal == "Monkey" or animal == "Gorilla":
    print("{} eats bananas".format(animal))
else:
    print("We don't know the food eaten by {}".format(animal))