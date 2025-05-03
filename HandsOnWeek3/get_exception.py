import traceback

try:
    # a = 7/0
    a = int(input("Enter your Integer: "))
except Exception as e:
    traceback.print_exc()
    print(e.__class__.__name__)
    print(e.__traceback__)