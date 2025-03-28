# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'

"""

# Your Code Below:

def grow_string(string_to_grow):
    ret_str = ""
    str_len = len(string_to_grow)
    idx = 1
    while idx <= str_len:
        ret_str += string_to_grow[:idx]
        idx += 1
    return ret_str

print(grow_string("Code"))
print(grow_string("abc"))




































# Solution:

# def grow_string(str):
#   result = ""
#   # On each iteration, add the substring of the chars 0..i
#   for i in range(len(str)):
#     result = result + str[:i+1]
#   return result

