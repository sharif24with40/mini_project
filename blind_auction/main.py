from auction_art import logo
print(logo)

bids = {}  # Initialize an empty dictionary to collect all bids

while True:
    name = input("What is your name?: ")
    bid_amount = int(input("How much you bid?: $"))
    
    bids[name] = bid_amount  # Add the bid to the dictionary
    
    again = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if again != "yes":
        break

# Determine the winner by finding the maximum bid
winner_name = max(bids, key=bids.get)
winner_bid = bids[winner_name]
print(f"The winner is {winner_name} with a bid of ${winner_bid}.")
