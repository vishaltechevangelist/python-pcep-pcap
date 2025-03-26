# Assignment 5:

"""
Define a function called key_list_items that can accept an unlimited number
of lists along with another argument. The function should return
the second_folder to last item in the specific list specified by the user of the function.

Example:

    For example, the below function call should return: jan

    key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])

"""

# Your Code Below:
def key_list_items(str1, **kwargs):
    return kwargs[str1][-2]

second_folder = key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])
print(second_folder)

first_folder = key_list_items("things", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])
print(first_folder)










































# Solution:

# def key_list_items(key, **kwargs):
#     keys = kwargs[key]
#     return keys[-2]
#
# result = key_list_items("people", things=['book', 'tv', 'shoes'], people=['pete', 'mike', 'jan', 'tom'],
#                 ages=[20, 30, 40])
# print(result)