class InvalidAgeException(Exception):
    pass

age = int(input("Please enter your age: "))
try:
    if age < 18:
        raise InvalidAgeException
    else:
        print("Eligible for vote")
except InvalidAgeException:
    print("Exception occured: Invalid Age is passed")