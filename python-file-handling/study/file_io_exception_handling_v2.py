try:
    my_file = open("sample.txt", "r")
    try:
        content = my_file.read()
    except IOError:
        print("Issue with working with the file")
    finally:
        my_file.close()
        print("This will always run regardless whether we have and exception or not")
except:
    print("Some error happened")