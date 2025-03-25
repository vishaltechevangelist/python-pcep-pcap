my_tuple = (1, 2, 3, "vishal", [1, 2, 'ha ha']) # using parentheses
# accessing element in tuple
print(my_tuple[4])
my_tuple[4][2] = 3
print(my_tuple)

## throw error while changing tuple element
#my_tuple[2] = 'saxena'

# count function similar to list
count = my_tuple.count("vishal")
print(count)

# slice similar to list, print gives tuple or correct data
print(my_tuple[:3])
print(my_tuple[3:])
print(type(my_tuple[1:2]))
print(type(my_tuple[4]))
