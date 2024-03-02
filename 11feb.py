# File Handling Adventures: Imagine you're an explorer in a text-based adventure 
# game. Create a Python script that reads a file named "treasure_map.txt" that 
# contains clues to find hidden treasures. As you read each clue, display it 
# with excitement and reveal the final treasure location at 
# the end

# file = open("treasure_map.txt","w")

# print(file.read())
# for i in file:
#     print(i)


# Become a detective tasked with solving a mystery using JSON data. You've received a JSON file containing clues about a stolen artifact. Write a Python program to extract and analyze the

import json

file = open("clues.json",'w')

with open('clues.json') as f:
    data = json.load(f)

artifact_name = data['artifact']['name']
theft_location = data['theft']['location']
theft_date = data['theft']['date']
suspects = data['suspects']

print(artifact_name,theft_location,theft_date,suspects)