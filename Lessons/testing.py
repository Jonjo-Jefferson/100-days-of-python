import random

print("Welcome to rock paper scissors!")
print("What is your choice? 0 = Rock, 1 = Paper, 2 = Scissors")

user_choice = int(input())
computer_choice = random.randint(0, 2)
win = "You win!"
lose = "You lose!"
draw = "Its a draw!"

if user_choice == 0:
    print("You picked rock!")
    if computer_choice == 0:
        print("Computer picked rock!")
        print(draw)
    if computer_choice == 1:
        print("Computer picked paper!")
        print(lose)
    if computer_choice == 2:
        print("Computer picked scissors!")
        print(win)

if user_choice == 1:
    print("You picked paper!")
    if computer_choice == 0:
        print("Computer picked rock!")
        print(win)
    if computer_choice == 1:
        print("Computer picked paper!")
        print(draw)
    if computer_choice == 2:
        print("Computer picked scissors!")
        print(lose)

if user_choice == 2:
    print("You picked scissors!")
    if computer_choice == 0:
        print("Computer picked rock!")
        print(lose)
    if computer_choice == 1:
        print("Computer picked paper!")
        print(win)
    if computer_choice == 2:
        print("Computer picked scissors!")
        print(draw)
