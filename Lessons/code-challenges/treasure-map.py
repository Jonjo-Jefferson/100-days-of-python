# 🚨 Don't change the code below 👇
row1 = ["11", "️21", "️31"]
row2 = ["12", "22", "️32"]
row3 = ["13️", "23", "33️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column = int(position[0])
row = int(position[1])

row -= 1
column -= 1

map[row][column] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
