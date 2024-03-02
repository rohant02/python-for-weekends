import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why was the math book sad? Because it had too many problems.",
    "What did one ocean say to the other ocean? Nothing, they just waved.",
    "What do you call fake spaghetti? An impasta!",
    "Why couldn't the bicycle stand up by itself? It was two-tired.",
    "Why did the tomato turn red? Because it saw the salad dressing!"
]

while True:
    user_input = input("Do you want to hear a joke? (yes/no): ").lower()
    if user_input == "yes":
        print(random.choice(jokes))
    elif user_input == "no":
        print("Okay, maybe next time!")
        break
    else:
        print("Sorry, I didn't understand that. Please enter 'yes' or 'no'.")
