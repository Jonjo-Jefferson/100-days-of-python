# LEAP YEAR CALCULATOR

year = int(input("Which year do you want to check? "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("Leap year")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# Basic Pizza Toppings

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

total_bill = 0

if size == "S":
    total_bill += 15
    if extra_cheese == "Y":
        total_bill += 1
    if add_pepperoni == "Y":
        total_bill += 2

elif size == "M":
    total_bill += 20

    if extra_cheese == "Y":
        total_bill += 1
    if add_pepperoni == "Y":
        total_bill += 3
else:
    total_bill += 25

    if extra_cheese == "Y":
        total_bill += 1
    if add_pepperoni == "Y":
        total_bill += 3

print(f"Your final bill is: ${total_bill}.")