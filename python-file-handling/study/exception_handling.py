def sum(num1, num2):
    try:
        print(num1+num2) # Error in this block, except take control execute the remaining instruction
    except:
        print("There was an error")

num1 = input("Enter a number = ")
sum(num1, 2)