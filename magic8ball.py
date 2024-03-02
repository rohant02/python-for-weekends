import random


def magicball():
    question = input("Enter your question: ")
    responses = ['yes','no','try again later']
    return random.choice(responses)

print(magicball())