import os

for dir_path, list_of_dirs, list_of_files in \
        (os.walk("/Users/vishalsaxena/Documents/python-pcep-pcap/python-file-handling/study/testing")):
    print(dir_path)
    print(list_of_dirs)
    print(list_of_files)
    print("\n=====")

print(os.environ.get("HOME")) # return HOME environment variable for me /Users/vishalsaxena

# generating path using environ variable to handle slash in the path
print(os.path.join(os.environ.get("HOME"), "myfile.txt"))

# get basename file name from the any path e.g check.txt
print(os.path.basename("/hahah/heheh/check.txt"))

# get directory name from any path e.g /hahah/heheh
print(os.path.dirname("/hahah/heheh/check.txt"))

# to get both path and basefile name in tuple
print(os.path.split("/hahah/heheh/check.txt"))

# to get filename and extension
print(os.path.splitext("/hahah/heheh/check.txt"))

# used to check path exist (return True) or not (return False)
print(os.path.exists("/hahah/heheh/check.txt"))

