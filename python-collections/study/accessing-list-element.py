# nested list
my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', 'banana'], 'd']

# To get banana
print(my_list[6][2])

# nested-nested list
my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', ['vishal', 'priyanka'], 'banana'], 'd']
# To get name=vishal
print(my_list[6][2][0])

# modifying content nested-nested list (yes)
my_list[2] = 'computer'
print(my_list)

# change priyanka to joe
my_list[6][2][1] = 'joe'
print(my_list)
