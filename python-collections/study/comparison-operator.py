# == (double equal) used to compare lhs with rhs based on value & type returns True or False
print(10==10) # True
print(10==9)  # False
print('Hello' == 'hello')  # False
print(5 == '5')  # False

# <  (less than) operator
print(5<10) # True

# > (greater than) operator
print(5>5) # False

# >= (greater than equal to) operator
print(5>=5) # True due to equality

# != (not equal) operator
print(5 != 6)   # True
print('5' != 5) # True
print('hello' != 'Hello') # True

# combining with logical operator
print((('hello' == 'Hello') or (5 == 5)) and ('8' != '8')) # False as last expression with 'and' is False

# not keyword operator, reverse/opposite the value
print(not 5)
condition = not (5==5)
print(condition)
