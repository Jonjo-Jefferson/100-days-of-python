import random

print("You enter the cat dungeon!")
print("What is your name adventurer?")
name = input()
hp = 100
gold = 0
location = "Entrance"

print(
    f"Welcome {name}!! You are holding {gold} gold and currently have {hp} hp! And are standing in the {location}"
)

if location == "Entrance":
    print(f"You are now in the {location} Room")
    print("Which way do you go? ")
    direction = input("L F R ")
    if direction == "L":
        location = "Hidden"
        print(f"You are now in the {location} Room")
        print(
            f"{name}!! You are holding {gold} gold and currently have {hp} hp! And are standing in the {location} room!"
        )
        selection = input("Do you touch the hidden plate? (Y OR N) ")
        if selection == "Y":
            hp -= 10
            lost_hp = 10
            print(f"You were bitten by a snake and lost {lost_hp} hp!!")
            location = "Stairs"
            print(
                f"{name}!! You are holding {gold} gold and currently have {hp} hp! And are standing in the {location} room!"
            )
        elif selection == "N":
            gold = gold + 100
            gained_gold = 100
            print(f"You just got {gained_gold} gold!")
            location = "Stairs"
            print(
                f"{name}!! You are holding {gold} gold and currently have {hp} hp! And are standing in the {location} room!"
            )
    elif direction == "R":
        location = "Spike"
        print(f"You are now in the {location} Room")
        success = random.randrange(1, 10)
        print(success)
        if success <= 5:
            print("You fell on the spikes!")
            hp = hp - 25
            print(f"You just lost {hp} hp")
            location = "Floor 1"
else:
    print("Welcome to Floor 1")
    print(
        f"{name}!! You are holding {gold} gold and currently have {hp} hp! And are standing in the {location} room!"
    )

if location == "Stairs":
    print("Welcome to the stairs room")