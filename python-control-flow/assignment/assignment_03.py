# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""
# Your Code Below:
def sequence(haystack_list):
    search_sequence = [1, 2, 3]
    has_sequence = False
    length_of_loop = len(haystack_list) - len(search_sequence) + 1
    for i in range(0, length_of_loop):
        # print(i)
    # pass
        if (haystack_list[i] == search_sequence[0] and
                haystack_list[i + 1] == search_sequence[1] and
                haystack_list[i + 2] == search_sequence[2]):
            has_sequence = True
            break
    return has_sequence



print(sequence([1, 1, 2, 3, 1]))
print(sequence([1, 1, 2, 3]))
print(sequence([1, 1, 2, 4, 1]))
print(sequence([1, 1, 2, 1, 2, 3]))
print(sequence([1, 2]))
print(sequence([2,3,1]))
print(sequence([]))



































# Solution:

# def sequence(num_list):
#     # Note: iterate with length-2, so can use i+1 and i+2 in the loop
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i + 1] == 2 and num_list[i + 2] == 3:
#             return True
#     return False
