dict = {} # curly braces
dict = {'k1':'value'}
print(dict)

# accessing value, used key
print(dict['k1'])

dict = {'k1':'some data', '7':'other data', 'list': [9, 8, 7]}
dict['7'] = 'new value'
print(dict)

# dictionary can't be sorted, can be accessed through keys and values can be updated as below
print("\n")
people_weight = {'Vishal': 90, 'Priyanka': 54}
print(people_weight)
print(people_weight['Vishal'])
people_weight['Vishal'] = 80
print(people_weight)

# pop method with dictionary return value and remove the entries
print("\n")
print(people_weight.pop('Priyanka'))
print(people_weight)

# clear the structure
people_weight.clear()
print("Here is the dictionary {}".format(people_weight))
people_weight['Sudha'] = 68
print(people_weight)


# list in dictionary
print("\n")
people_weight['fruits'] = ['banana', 'orange']
print(people_weight)
print(people_weight['fruits'][1])

# nested dictionary
print("\n")
people_weight['fruits'][1] = {'1':'sweet orange', '2':'bitter orange'}
print(people_weight)
print(people_weight['fruits'][1]['2'])

# Tuple in dictionary
print("\n")
people_weight['tuple'] = ('a', 'b', 'c')
print(people_weight)
print(people_weight['tuple'][2])
#people_weight['tuple'][2] = 'd' # throws error as tuple can't be modified
my_tuple = people_weight.pop('tuple')
print(my_tuple)
print(people_weight) # tuple key removed