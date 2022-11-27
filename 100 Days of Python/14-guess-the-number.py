import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

DIFFICULTY = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts_remaining = 0
game_is_over = False
random_number = random.randint(0, 100)
print(random_number)
if DIFFICULTY == 'easy':
    attempts_remaining = 10
else:
    attempts_remaining = 5

while game_is_over == False:
    user_guess = input("Select a number between 1 and 100 :")
    if int(user_guess) < random_number:
        print(
            f"Sorry guess too low! You have {attempts_remaining} attempts left!"
        )
        attempts_remaining -= 1
        if attempts_remaining == 0:
            game_is_over = True
    elif int(user_guess) > random_number:
        print(
            f"Sorry guess too high You have {attempts_remaining} attempts left!"
        )
        attempts_remaining -= 1
        if attempts_remaining == 0:
            game_is_over = True
    else:
        print("You guessed right!")
        game_is_over = True

if game_is_over == True and attempts_remaining > 0:
    print(f"You win with the number {random_number}")
elif game_is_over == True and attempts_remaining == 0:
    print(f"You lose! The humber was {random_number}")
