for num in range(10):
    print(num)

# range start from 5 instead of default 0
print("Printing from 5")
for num in range(5, 10): # 10 is non-inclusive
    print(num)

print("Printing with step")
for num in range(5, 10, 2):
    print(num)

# printing even numbers only
for num in range(0, 10, 2):
    print("The even number {}".format(num))

# Zip function
print(list(zip('abcdefg', range(3), range(4))))

# enumerate function
mylist = ['Dinesh', 'Sudha', 'Vishal', 'Priyanka', 'Adharv', 'Advik']
for listItem in enumerate(mylist):
    print(listItem) # Tuple have sequence number along with items

for listItem in enumerate(mylist, 1):
    print(listItem) # Tuple have sequence number along with items

#### More Handy utility ####
list_a = ['a', 'b', 'c', 'd', 'e', 'f']
print('z' in list_a) # if z exists in list_a

# checking in dictionary
print('john' in {'john': 140}) # checks only key exist, return True
print(140 in {'john': 140}) # return False, don't check values hence for below code will check
print(140 in {'john': 140}.values())

### Math function - min, max, random
list_a = ['a', 'c', 'd']
list_b = [1,2,3,4,5]
print(min(list_b))
print(max(list_b))
print(min(list_a))
print(max(list_a))

#### Generate random number
from random import randint
print(randint(0, 1000))

#### Shuffle the list
from random import shuffle
my_list = [1, 2, 3, 4, 5]
shuffle(my_list)
print(my_list)


#### Shuffle number list
num_list = list(range(1, 101))
shuffle(num_list)
print(num_list)


