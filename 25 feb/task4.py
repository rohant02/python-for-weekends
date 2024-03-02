# Implement a Python function that generates a 
# sequence of even numbers up to a given limit using a generator.

def evengenerator(limit):
    a = 0
    while a<limit:
        yield a
        a+=2
sequence = list(evengenerator(20))
print(sequence)