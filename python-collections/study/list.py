my_list = []
print(my_list)
print(type(my_list))

my_list = [1, 2, 3, 4, 5]
print(my_list)

popped_value = my_list.pop() # remove the last value from the list
print("The new list is {}".format(my_list))
print("Popped value is {}".format(popped_value))

my_list.pop(2) # remove the second index from the list
print(my_list)

my_list[0] = "Vishal" # list are mutable hence value can be changed
print(my_list)        # list can contain mixed data type e.g int, str, object(list)

my_list[0] = ["Vishal", "Saxena"]
print(my_list)        # list can contain mixed data type e.g int, str, object(list)

my_list.append("Hi My name is vishal")
print(my_list)

my_list.append([20, 10, 30])
print(my_list)
popped_value = my_list.pop()
print(popped_value)


print("Checking sorting")
print(my_list)
#my_list.sort()
#print(my_list)

print("\n Checking reverse")
print(my_list)
my_list.reverse()
print(my_list)

print("\n checking with alpha list")
alpha_list = ['a', 'z', 'd', 'p']
alpha_list.sort()
print(alpha_list)
alpha_list.reverse()
print(alpha_list)
print(alpha_list[2:4]) # action is same as string
print(len(alpha_list))

print("Merge list")
print(my_list + alpha_list)