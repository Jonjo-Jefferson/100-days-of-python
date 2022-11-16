fruits = ['Apple', 'peace', 'pear']

for fruit in fruits:
    print(fruit)

for number in range(0, 20):
    print(number)

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 119
gpa = 1

if not credits >= 110:
    print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
    print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0):
    print("You do not meet either requirement to graduate!")

print(not True == False)

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
    print("You meet the requirements to graduate!")
else:
    print("YOu do not meet the requirements to graduate.")
