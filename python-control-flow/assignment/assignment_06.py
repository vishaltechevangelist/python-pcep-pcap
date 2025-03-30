# Assignment 6

"""
Create a function called last2 that accepts a string argument.
The function should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your function should look for in the remaining string.

So "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

"""
# Your Code Below:

def last2(str):
    count = 0
    mod_str = str[0:-2]
    last_2 = str[-2:]
    for idx in range(len(mod_str) - 1):
        if mod_str[idx] == last_2[0] and mod_str[idx + 1] == last_2[1]:
            count += 1
    # if last_2 in str[0:-2]:
    #     count = mod_str.count(last_2)
    return count

print(last2('hixxhi')) #→ 1
print(last2('xaxxaxaxx')) #→ 1
print(last2('axxxxaaxx')) #→ 3
print(last2("vi"))





























# Solution

# def last2(str):
#     # Screen out too-short string case.
#     if len(str) < 2:
#         return 0
#
#     # last 2 chars, can be written as str[-2:]
#     last2 = str[len(str) - 2:]
#     count = 0
#
#     # Check each substring length 2 starting at i
#     for i in range(len(str) - 2):
#         sub = str[i:i + 2]
#         if sub == last2:
#             count = count + 1
#
#     return count
