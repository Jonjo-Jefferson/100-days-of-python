year = int(input("Which year do you want to check? "))

divide_one_hundred = year / 100
divide_four_hundred = year / 400

# DEBUG

# print(divide_four)
# print(divide_one_hundred)
# print(divide_four_hundred)

if (year % 4) != 0:
    print("Not leap year")
elif (year % 2) == 0:
    if (divide_one_hundred % 2) != 0:
        print("Leap year")
    else:
        if (divide_four_hundred % 2) == 0:
            print("Leap year")
        else:
            print("Not leap year")
