# 1. Lambda Functions:
# Task: Create a superhero-themed lambda function that doubles the power of each superhero. Apply it to a list of superhero abilities.

double_power = lambda power: power * 2

superhero_abilities = ['super strength', 'flight', 'telekinesis', 'super speed']

superhero_ability_number = [2,5,3,7]

#double_ability = [double_power(ability) for ability in superhero_ability_number]
double_ability = [double_power(ability) for ability in superhero_abilities]
print(superhero_abilities)
print(double_ability)
# print(double_ability)
# 2. Code Documentation:
# Task: Write a Python function that simulates a magic spell. Add whimsical docstrings describing the mystical incantations and 
# expected enchantments.
# 3. Map, Filter, Reduce:
# Task: Use map() to transform a list of candy names into a list of their deliciousness ratings. 
# For example, from ["chocolate", "gummy bears", "caramel"], rate them from 1 to 10.

# def rate_deliciousness(candy):
#     deliciousness_ratings = {
#         "chocolate": 9,
#         "gummy bears": 7,
#         "caramel": 8
#     }
#     return deliciousness_ratings.get(candy, 0)

# candy_names = ["chocolate", "gummy bears", "caramel"]

# ratings = list(map(candy_names,rate_deliciousness))

# for candy, rating in zip(candy_names, ratings):
#     print(f"{candy}: {rating}/10")
# 4. Decorators:
# Task: Create a decorator named "Party Time" that adds confetti and sparkles to any function. 
#Use it to enhance your party-planning functions.