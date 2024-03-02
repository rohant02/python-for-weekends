# Exercise 1 (Functional Programming): Create a Python function that takes a list of integers as input and returns a 
# new list with each element squared.

# def functions_squared(listofnumbers):
#     res= []
#     for x in listofnumbers: 
#         res.append(int(x)**2)

#     return res

# list1= input("Enter a list of numbers: ")
# int_list = list1.split(",")
# print(functions_squared(int_list))

# Exercise 2 (Functions and Arguments): Write a Python function that calculates and returns the average of a list of numbers.
# listofnumbers = [432948,23213,10000]
# def functions_average(listofnumbers):
#      total = 0
#      count = 0
#      for x in listofnumbers: 
#          print(x)
#          total = x + total

#          count = count+1

#      return (total/count)


# print(functions_average(listofnumbers))



# list1= input("Enter a list of numbers: ")
# int_list = list1.split(",")
# print(functions_squared(int_list))


# Exercise 3 (Scope of Visibility): Define a variable inside a function and print its value both inside and outside the function. 
# Observe how scope affects variable visibility.

# var1 = 6
# print(var1)
# def variablescope():
#      var1 = 5
#      print(var1)

# variablescope()

# Exercise 4 (List Generators): Use a list comprehension to generate a list of the first 10 positive even numbers.

def listofeven(n):
    return [x*2 for x in range(1,n+1) ]
    #x*2 

    # for x in range(1, n+1):
    #     res=x*2
    #     print(res)

print(listofeven(15))


# Exercise 5 (Annotations): Write a Python function to calculate the area of a circle based on its radius, and add 
# function annotations to specify the types of the arguments and the return type.

# from math import pi

# def areaofcircle(r:int) -> int:
#     area = pi * r ** 2
#     print(area)

# areaofcircle(5)



# def listinputtaker():
#     lst = []

#     n = int(input("Enter number of elements : "))

#     for i in range(0, n):
#         thespecificinput = int(input())
    
#         lst.append(thespecificinput)  
 
#     print(lst)

# listinputtaker()