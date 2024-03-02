# 
# Assignment 1: Creating a Personal Chatbot
# Create a simple chatbot in Python that responds to questions and executes user commands.
# Requirements:
# Write a program that greets the user and asks for their name.
# The program should respond to questions like "How are you?" or "What's your name?"
# Include at least three questions and responses to make the chatbot more interesting.
# Hint: Use conditional statements (if, elif, else) to determine the bot's response to different questions.
# Submission: Share the Python code for your chatbot and a screenshot of a conversation with it.


print("Hello! I'm your personal chatbot.")
name = input("What's your name? ")
print(f"Nice to meet you, {name}!")

while True:
    user_input = input("You: ").lower()
    if user_input == "how are you?":
        print("Bot: I'm just a program, so I don't have feelings, but thanks for asking!")
    elif user_input == "what's your name?":
        print("Bot: I'm just a simple chatbot.")
    elif user_input == "how old are you?":
        print("Bot: I don't have an age. I'm just lines of code.")
    elif user_input == "exit":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")
