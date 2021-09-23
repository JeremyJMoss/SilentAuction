from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
should_continue = True

def create_bidder(bidder_name, bid_ammount):
  bidder = {}
  bidder["name"] = bidder_name
  bidder["bid"] = bid_ammount
  bidders.append(bidder)

bidders = []

while should_continue == True:
  print(logo)
  name = input("What is your name?: ")  
  bid = int(input("What is your bid?: $"))
  repeat = input("Are there any other bidders? Type 'yes' of 'no'.\n")
  
  if repeat == "no":
    should_continue = False
  
  create_bidder(name, bid)
  clear()

max_bidder = {
  "name": "",
  "bid": 0
}

for key in bidders:
  if key["bid"] > max_bidder["bid"]:
    max_bidder["bid"] = key["bid"]
    max_bidder["name"] = key["name"]

print(f"The winner is {max_bidder['name']} with a bid of ${max_bidder['bid']}.")
