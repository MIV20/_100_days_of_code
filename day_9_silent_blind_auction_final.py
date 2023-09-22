from replit import clear
from day_9_art import logo

print(logo)

item_bidders = {}
bidding_finished = False


def get_winner(auction_bidder):
    highest_bid = 0
    winner = ""
    for bidder in auction_bidder:
        bid_amount = auction_bidder[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}!")


while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid: $"))
    item_bidders[name] = bid
    no_more_bidders = input(f"Are there more bidders on this item? Type yes or no?")
    if no_more_bidders == "no".lower():
        bidding_finished = True
        get_winner(item_bidders)
    elif no_more_bidders == "yes".lower():
        clear()

