try:
    with open("sample.txt", "r") as file:
        content = file.read()
        # result = 2 + '2'
except TypeError: # Error is actually file not found error this error will stop execution
    print("This might be TypeError after adding 2 + '2'")
except FileNotFoundError:
    print("File does not exist : FileNotFoundError")
except: # Will catch all general exception
    print("Error logged to the system")
finally:
    print("This will always run regardless whether we have and exception or not")

print("This line will run i.e there is no exception or handle gracefully")