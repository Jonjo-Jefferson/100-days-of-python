import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

player_cards = []
dealer_cards = []


def deal_cards():
    for i in range(2):
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    player_count = sum(player_cards)
    dealer_count = sum(dealer_cards)
    print("Players cards: ",
          str(player_cards) + " which equals " + str(player_count))
    print("Dealers cards: ",
          str(dealer_cards) + " which equals " + str(dealer_count))
    player_count = sum(player_cards)
    dealer_count = sum(dealer_cards)
    while dealer_count < 17:
        dealer_cards.append(random.choice(cards))
        dealer_count = sum(dealer_cards)
        print("Dealers hits: ",
              str(dealer_cards) + " which equals " + str(dealer_count))
    while player_count < 17:
        player_cards.append(random.choice(cards))
        player_count = sum(player_cards)
        print("Dealers hits: ",
              str(player_cards) + " which equals " + str(player_count))


deal_cards()
