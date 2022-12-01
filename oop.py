# from turtle import Turtle, Screen

# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["pikachu", "bacok", "hihi"])
table.add_column("Type", ["hot", "cold", "stone"])

table.align = "l"
print(table)
