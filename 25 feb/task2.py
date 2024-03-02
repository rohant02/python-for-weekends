# 2.Write a Python function that generates a 
# Fibonacci sequence up to a given limit using a generator.

def fibonacci(limit):
    a,b = 0,1
    while a<limit:
        yield a
        a, b = b, a+b
        print(a,b)
sequence = list(fibonacci(300))
print(sequence)
