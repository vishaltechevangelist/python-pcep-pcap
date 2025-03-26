#help(print)

# Defining the function
def greet_person():
    print("Hello there, How are u?")

def greet_person_with_name(name = 'Priyanka'): # Function definition has name Parameter
    '''
    This is docstring used to documentation in python
    INPUT: name
    OUTPUT: Hello {name}, How are u?
    '''
    print("Hello {}, How are u?".format(name))

def greet_person_with_name_v2(name = 1):
    print("Hello {}, How are u?".format(name))

def greet_person_with_return(name = 'Python'):
    return "Hello {}, I am good!".format(name)

def get_remainder(num1, num2):
    """
    :param num1: This is 1st number
    :param num2: This is 2nd number
    :return: remainder using modulus operator
    """
    return num2 % num1

# Calling the function
greet_person()
greet_person_with_name('Vishal') # function call with argument 'Vishal'
greet_person_with_name()
greet_person_with_name_v2()

return_str = greet_person_with_return()
print(return_str)

remainder = get_remainder(3, 10)
print(remainder)
