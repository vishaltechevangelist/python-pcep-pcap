my_list = ['b', 'd', 'a', 'z', 'x']
another_list = [1, 2, 3, 4, 5]

# output ['d', 'b', 'a', 3, 2, 1]

new_my_list = my_list[:3]
new_my_list.sort()
new_my_list.reverse()
print(new_my_list)
new_another_list = another_list[:3]
new_another_list.reverse()
print(new_another_list)

resulted_list = new_my_list + new_another_list
print(resulted_list)

# print("\nUsing append")
# new_my_list.append(new_another_list)
# print(new_my_list)