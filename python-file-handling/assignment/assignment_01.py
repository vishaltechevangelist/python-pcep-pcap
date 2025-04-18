# Assignment 1:

import sys
import os
import re

# directory_containing_files = \
"/Users/vishalsaxena/Documents/python-pcep-pcap/python-file-handling/assignment/project_files" #sys.argv[1]
# words_to_aggregate = ["hello", "Peter", "computer"] #sys.argv[2:]
directory_containing_files = sys.argv[1]
words_to_aggregate = sys.argv[2:][0].split(",")

# Expected Output:
# {"there": n, "Michael": n, "running": n}

# Your Code Below:
word_count = {}
for dir_path, dir_list, file_list in os.walk(directory_containing_files):
    for file_name in file_list:
        with open(os.path.join(dir_path, file_name)) as sel_file:
            content = sel_file.read()
            for word in words_to_aggregate:
                word_occurance_list = re.findall(word, content)
                # first_key = os.path.splitext(file_name)[0]
                if word in word_count.keys():
                    word_count[word] += len(word_occurance_list)
                else:
                    word_count.update({word:len(word_occurance_list)})
                print("The dictionary like {} from {}".format(word_count, file_name))


print(word_count)











































#Solution:
# words_and_counts = {}
#
# for word in words_to_aggregate:
#     count = 0
#     for path, folder_names, file_names in os.walk(directory_containing_files):
#         for file_name in file_names:
#             file = os.path.join(path, file_name)
#             with open(file, "r") as a_file:
#                 for line in a_file:
#                     if re.search(word, line):
#                         word_list = re.findall(word, line)
#                         count += len(word_list)
#
#     words_and_counts[word] = count
#
#
#
# print(words_and_counts)