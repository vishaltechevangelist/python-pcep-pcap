
if __name__ == '__main__':
    myfile = open("sample.txt") # open the file
    content = myfile.read()
    # print(content)

    print("--------------")
    myfile.seek(0) # reset the cursor, take it to the beginning
    data = myfile.read()
    # print(data) # This not get printed

    myfile.seek(0) # reset the cursor, take it to the beginning
    content_list = myfile.readlines()
    # print(content_list)

    myfile.close() # close the file as it might be used by other execution

    # with open("sample.txt", "a") as my_file: # open file and close implicitly once out the block or execution complete
        # new_content = my_file.read()
    with open("sample.txt", "w") as my_file:
        my_file.write("\nTHIS IS MY SENTENCE")

    my_appended_file = open("sample.txt")
    print(my_appended_file.read())
    my_appended_file.close()

    # mode a => append, w => overwrite, create new

