import json

dic1 = {'name': 'rohan', 'age': 21}

# Writing to the file
with open('rohan.json', 'w') as file:
    json.dump(dic1, file)

# Reading from the file
with open('rohan.json', 'r') as file:
    dict1 = json.load(file)
    print(dict1)
