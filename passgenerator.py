import random


def generatepass(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = "".join(random.choice(characters) for i in range(length))

    return password

# print(generatepass(15))
# lenofpass = int(input("Enter number of characters"))
# print(generatepass(lenofpass))

def main():
    while True:
        lenofpass = int(input("Enter number of characters"))
        print(generatepass(lenofpass))
        userans = input("Would you like to continue? (y/n)")
        if userans != "y":
            print("Thanks for using the program!")
            break

main()