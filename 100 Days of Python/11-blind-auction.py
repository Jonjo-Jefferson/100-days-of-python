import os

bidders = {}
max_bid = 0
max_bidder = ""


def blind_auction():
    any_other_bidders = True
    while any_other_bidders == True:
        for i in range(1):
            name = input("Input your name: ")
            bid = input("Input your bid: ")
            bidders[name] = bid
            any_other_bidders = input(
                "Are there any other bidders? Y or N ").upper()
            if any_other_bidders == "Y":
                any_other_bidders = True
                os.system('cls')
            else:
                any_other_bidders = False
                print(bidders)
                max_bid = max(bidders.values())
                max_name = max(bidders, key=bidders.get)

                print(
                    f"And the winner is.... {max_name} with a bid of {max_bid}!"
                )


blind_auction()
