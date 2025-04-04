
# Assignment 5

"""
Define a method that accepts a list as an argument
and returns True if one of the first_folder 4 elements
in the list is a 6. The list length may be less than 4.


first3([1, 2, 6, 3, 4]) → True
first3([1, 2, 3, 4, 6]) → False
first3([1, 2, 3, 4, 5]) → False

"""

# Your Code Below:
def first3(num_list):
    six_exist = False
    if 6 in num_list[:4]:
        six_exist = True
    return six_exist

# print(first3([1, 2, 6, 3, 4]))
# print(first3([1, 2, 3, 4, 6]))
# print(first3([1, 2, 3, 4, 5]))

print(first3([1,2,6,3,0,0])) # True
print(first3([1,2,3,3,0,6])) # False
print(first3([6])) # True
print(first3([])) # False



























# Solution:

# def first3(numbers):
#     # First figure the end for the loop
#     end = len(numbers)
#     if end > 4:
#         end = 4
#
#     for i in range(end):  # loop over index [0, 1, 2, 3]
#         if numbers[i] == 6:
#             return True
#     return False
