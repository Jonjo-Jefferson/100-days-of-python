import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_name = random.randint(0, len(names))

print(f"{names[random_name]} is going to buy the meal today!")

# print(f"{} is going to buy the meal today!")

fruits = [
    "Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
    "Pears"
]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])