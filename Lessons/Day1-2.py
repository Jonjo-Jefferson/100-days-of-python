# print("Hello World!\nHello World!")
# print("Hello" + " " + "JJ")

# print(len(input("What is your name? ")))

# name = input("What is your name? ")
# length = len(name)
# print(length)

# a = input("a: ")
# b = input("b: ")

# a, b = b, a

# print("a: " + a)
# print("b: " + b)

# Subscripting

# print("Hello"[0])

# num_char = len(input("What is your name? "))

# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters")

# Coding exercise - data types

# two_digit_number = input("Type a two digit number: ")
# num1 = int(two_digit_number[0])
# num2 = int(two_digit_number[1])
# print(num1 + num2)

# coding exercise BMI calculator

# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# height = float(height)
# weight = int(weight)
# print(round(weight / (height * height)))

# bmi = int(weight) / float(height) ** 2
# bim_as_int = int(bmi)
# print(bim_as_int)

# floor division

# print(8 // 3)

# score += 1
# score -= 1

# f-string

# score = 0
# height = 1.8
# is_winning = True

# print(f"your score is {score}, your height is {height} and you are {is_winning}")

# age = input("What is your current age? ")
# difference_age = 90 - int(age)
# days = difference_age * 365
# weeks = difference_age * 52
# months = difference_age * 12
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")

print(6 + 4 / 2 - (1 * 2))

# name = "bacon"
# dad = "pro ganja smoker"

# print(f"My name is {name} and my dad is {dad}")

# food_list = ["bacon", 23, "tomato", 32, "onion", "potato", "bagel"]

name = input("What is your name? ")
age = input("How old are you? ")

print(type(age))
calculate_age_in_weeks = int(age) * 52

print(f"{name} you are {age} and in weeks that is {calculate_age_in_weeks}")