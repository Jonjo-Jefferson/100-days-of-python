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

# -------------------------------------------- ORIGINAL CODE ------------------------------------------------------------

# import random

# print("0 for Rock, 1 for Paper, 2 for Scissors")
# user = int(input())

# print(type(user))

# computer = random.randint(0, 2)

# print(f"Computer choice in value {computer}")

# if computer == 0:
#     computer = "Rock"
# elif computer == 1:
#     computer = "Paper"
# else:
#     computer = "Scissors"

# if user == 0:
#     user = "Rock"
# elif user == 1:
#     user = "Paper"
# else:
#     user = "Scissors"

# print(f"Computer picked {computer}")
# print(f"You picked {user}")

# rock = "Rock"
# paper = "Paper"
# scissors = "Scissors"

# win = "YOU WIN!"
# lose = "YOU LOSE!"
# draw = "ITS A DRAW!"

# if computer == "Rock":
#     if user == "Rock":
#         print(f"You both picked {rock}!")
#         print(f"{draw}")
#     elif user == "Paper":
#         print(f"You picked {paper} and computer picked {rock}")
#         print(f"{win}")
#     else:
#         print(f"You picked {scissors} and computer picked {rock}")
#         print(f"{lose}")

# elif computer == "Paper":
#     if user == "Paper":
#         print(f"You picked {rock} and computer picked {paper}")
#         print(f"{lose}")
#     elif user == "Paper":
#         print(f"You both picked {paper}")
#         print(f"{draw}")
#     else:
#         print(f"You picked {scissors} and computer picked {paper}")
#         print(f"{win}")

# else:
#     if user == "Rock":
#         print(f"You picked {rock} and computer picked {scissors}")
#         print(f"{win}")
#     elif user == "Paper":
#         print(f"You picked {paper} and computer picked {scissors}")
#         print(f"{lose}")
#     else:
#         print(f"You picked {scissors} and computer picked {scissors}")
#         print(f"{draw}")
