# Iterating through list
farm_animals = ['Goat', 'Horse', 'Chicken', 'Cow', 'Dog']
for animal in farm_animals:
    idx = farm_animals.index(animal) + 1
    print("{}. {} is safe in our farm".format(idx, animal))

# Iterating through tuple (this example is similar to list iteration)
farm_animals = ('Goat', 'Horse', 'Chicken', 'Cow', 'Dog')
for animal in farm_animals:
    idx = farm_animals.index(animal) + 1
    print("{}. {} is safe in our farm".format(idx, animal))

# Iterating through string
greeting = "Hello, my name is Vishal"
for char in greeting:
    print(char)

# Breaking the iteration combining with condition
for break_char in greeting:
    if break_char == "n":
        break
    print(break_char)

# Use continue to skip the current iteration and move to next iteration
for break_char in greeting:
    if break_char == "n":
        continue # it skip n break_char iteration
    print(break_char)
