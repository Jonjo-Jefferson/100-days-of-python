import random


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return score calculated"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


user_cards = []
dealer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

user_score = calculate_score(user_cards)
dealer_score = calculate_score(dealer_cards)

print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Dealers cards: {dealer_cards[0]}")

if user_score == 0 or dealer_cards == 0 or user_score > 21:
    is_game_over = True

while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

# import random

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

# player_cards = []
# dealer_cards = []

# def deal_cards():
#     for i in range(2):
#         player_cards.append(random.choice(cards))
#         dealer_cards.append(random.choice(cards))
#     player_count = sum(player_cards)
#     dealer_count = sum(dealer_cards)
#     print("Players cards: ",
#           str(player_cards) + " which equals " + str(player_count))
#     print("Dealers cards: ",
#           str(dealer_cards) + " which equals " + str(dealer_count))
#     player_count = sum(player_cards)
#     dealer_count = sum(dealer_cards)
#     while dealer_count < 17:
#         dealer_cards.append(random.choice(cards))
#         dealer_count = sum(dealer_cards)
#         print("Dealers hits: ",
#               str(dealer_cards) + " which equals " + str(dealer_count))
#     while player_count < 17:
#         player_cards.append(random.choice(cards))
#         player_count = sum(player_cards)
#         print("Dealers hits: ",
#               str(player_cards) + " which equals " + str(player_count))

# deal_cards()
