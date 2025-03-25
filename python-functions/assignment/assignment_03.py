# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.

The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.

"""
from re import split

# Your Code Below:
def multi_merge(list1, str1):
    list_from_str = list(str1)
    words_from_str = split(' ', str1)
    return list1 + words_from_str + list_from_str

list1 = [1, 2, 3]
str1 = 'vishal saxena'
resulted_list = multi_merge(list1, str1)
print(resulted_list)








































# Solution:

# def multi_merge(list_a, str):
#     return list_a + str.split() + list(str)
#
# print(multi_merge([1,2,3,4], "Hello My name is imtiaz"))
