# 1. Write a program that asks the user to enter a number and then prints its square. Use a try/except block to handle possible input errors.
# import math
# number = input("enter a number:")

# try:
#     number1 = int(number)
#     result = math.pow(number1,2)
#     print(result)
# except:
#     print("error")
# else:
#     print("there is no error")
# finally:
#     print("always executes")

# 2. Create a function that divides two numbers, prompting them from the user. Handle the division by zero exception.

import math
# number1 = input("enter a first number: ")   
# number2 = input("enter a second number: ")  

# def function1(number1,number2):
#     try:
#         number1/number2
#     except ZeroDivisionError:
#         print("0 division")

# function1(number1,number2)

# 3. Write a program that generates a random number from 1 to 10 and asks the user to guess it. 
#    Handle the ValueError exception for incorrect input.

# import random

# #randomguess = int(input("enter a number: "))

# number = random.randint(1,3)

# try:
#     randomguess = int(input("enter a number: "))
#     if number == randomguess:
#         print("that is the correct guess")
#     else:
#         print("that is incorrect guess")  
#         print(f"the number is : {number}")  
# except ValueError:
#     print("value error")
# except:
#     print("there is an error")    



# 4. Create a list of numbers and try to access an element with an index that is out of range. Handle the IndexError exception.

# 5. Write a program that asks the user to enter a number. If the number is negative, raise a ValueError 
    # exception with the message "The number must be positive".

# number = int(input("enter a number: "))

try:
    number = int(input("enter a number: "))
    if number < 0:
        raise ValueError("the number should be positive")
except ValueError as e:
    print(e)
except:
    print("error")