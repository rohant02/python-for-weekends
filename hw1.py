
numbers = list(range(1, 11))


#even_squares = [x ** 2 for x in numbers if x % 2 == 0]
def even_squares(numbers):
    res = [x ** 2 for x in numbers if x % 2 == 0]
    print("List of squares of even numbers:", res)


print("Original list of numbers:", numbers)
#print("List of squares of even numbers:", even_squares)
even_squares(numbers)



#even_squares = [x ** 2 for x in numbers if x % 2 == 0]
#print("List of squares of even numbers:", even_squares)