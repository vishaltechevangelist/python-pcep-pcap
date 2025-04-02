import os

# get current working directory
print(os.getcwd())

# change current working directory
# os.chdir("/tmp")

print(os.getcwd())

# list current directory
print(os.listdir())

# create new directory
if "testing" not in os.listdir():
    os.mkdir("testing")
    # create nested directory
    os.makedirs("testing/sub_testing/data")

# remove empty child directory only
# os.rmdir("testing/sub_testing/data")

# remove specific file
# os.remove("testing/sub_testing/test.txt")

# never runs be cautious
# os.removedirs("testing/sub_testing")

os.rename("sample.txt", "testing/sub_testing/data/renamed.txt")

