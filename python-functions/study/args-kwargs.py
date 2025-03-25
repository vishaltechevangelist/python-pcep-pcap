"""
*args unlimited number of positional parameter in tuple form
**kwargs unlimited number of keywords-value parameter in dictionary form
"""

def mysum(*args):
    return len(args)


print(mysum(9,8,7, 65, 10))


def key_value_fun(**kwargs):
    print("The key are {}".format(kwargs.keys()))
    print("The values are {}".format(kwargs.values()))
    print("The value of address is {}".format(kwargs.get('address')))
    print("The value of address is {}".format(kwargs.get('address1'))) # return None for non-existent key

key_value_fun(name="Vishal", age="24", address="Ghaziabad")