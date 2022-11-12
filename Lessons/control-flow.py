# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay £1")
#     elif age <= 18:
#         print("Please pay £4")
#     else:
#         print(("Please pay £23"))
# else:
#     print("You can NOT ride the rollercoaster!")

# ODD OR EVEN

# number = int(input("Which number do you want to check? "))

# if (number % 2) == 0:
#     print(number)
#     print("This is an even number")
# else:
#     print(number)
#     print("This is an odd number")

# BMI 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(int(weight) / float(height)**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
