try:
    even_number = [2,4,6,8,10]
    print(even_number[5])
except ZeroDivisionError:
    print("Denominator can't be zero")
except IndexError:
    print("Index is out of bound")