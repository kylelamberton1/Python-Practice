from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print (logo)
name_bid_dict = {}
another_bid = True
while another_bid:
  name = input("Welcome to 'Blind Auction'. What is your name?\n").lower()
  bid = int(input ("What is your bid?\n"))
  name_bid_dict [name] = bid
  new_bidder = input("Is there another bidder?\n").lower()
  
  if new_bidder == "no" or new_bidder == "n":
    another_bid = False
  elif new_bidder == "yes" or new_bidder == "y":
    clear()

maximum_person = max(name_bid_dict, key=name_bid_dict.get)
maximum_figure = (name_bid_dict[maximum_person])
print (f"{maximum_person} is the highest bidder with £{maximum_figure}")

##################################################################################################################################################################################
#HER SOLUTION#
#bids = {}
#bidding_finished = False

#def find_highest_bidder(bidding_record):
#  highest_bid = 0
#  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
#  for bidder in bidding_record:
#    bid_amount = bidding_record[bidder]
 #   if bid_amount > highest_bid: 
  #    highest_bid = bid_amount
   #   winner = bidder
#  print(f"The winner is {winner} with a bid of ${highest_bid}")
#
#while not bidding_finished:
 # name = input("What is your name?: ")
  #price = int(input("What is your bid?: $"))
  #bids[name] = price
#  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
 # if should_continue == "no":
 #   bidding_finished = True
  #  find_highest_bidder(bids)
 # elif should_continue == "yes":
  #  clear()