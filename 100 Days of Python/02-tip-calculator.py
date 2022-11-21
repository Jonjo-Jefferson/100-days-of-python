# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6


print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
tip = (
    float(input("What percentage tip would you like to give? 10, 12, or 15? "))
    / 100 + 1)
people = int(input("How many people to split the bill? "))
calculate_total = total_bill / people * tip
print(f"Each person should pay {round(calculate_total)}")
