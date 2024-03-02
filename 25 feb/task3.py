# 3.Create a Python program to iterate over 
# a dictionary and print key-value pairs using a generator.

dict1 = {'a':10,'b':15,'c':20}

def iterdict(dictionary):
    for key,value in dictionary.items():
        print(key,value)

result = iterdict(dict1)
print(result)
# for x in result:
#     print(x)