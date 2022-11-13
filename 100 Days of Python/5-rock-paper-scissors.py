import random

print("0 for Rock, 1 for Paper, 2 for Scissors")
user = int(input())

print(type(user))

computer = random.randint(0, 2)

print(f"Computer choice in value {computer}")

if computer == 0:
    computer = "Rock"
elif computer == 1:
    computer = "Paper"
else:
    computer = "Scissors"

if user == 0:
    user = "Rock"
elif user == 1:
    user = "Paper"
else:
    user = "Scissors"

print(f"Computer picked {computer}")
print(f"You picked {user}")

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

win = "YOU WIN!"
lose = "YOU LOSE!"
draw = "ITS A DRAW!"

if computer == "Rock":
    if user == "Rock":
        print(f"You both picked {rock}!")
        print(f"{draw}")
    elif user == "Paper":
        print(f"You picked {paper} and computer picked {rock}")
        print(f"{win}")
    else:
        print(f"You picked {scissors} and computer picked {rock}")
        print(f"{lose}")

elif computer == "Paper":
    if user == "Paper":
        print(f"You picked {rock} and computer picked {paper}")
        print(f"{lose}")
    elif user == "Paper":
        print(f"You both picked {paper}")
        print(f"{draw}")
    else:
        print(f"You picked {scissors} and computer picked {paper}")
        print(f"{win}")

else:
    if user == "Rock":
        print(f"You picked {rock} and computer picked {scissors}")
        print(f"{win}")
    elif user == "Paper":
        print(f"You picked {paper} and computer picked {scissors}")
        print(f"{lose}")
    else:
        print(f"You picked {scissors} and computer picked {scissors}")
        print(f"{draw}")
