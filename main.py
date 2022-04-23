from replit import clear
print("Welcome to the secret auction program.\n")
to_continue = "Yes"

#bidding_dict = {
#  "Bidders":[ ],
#  "Bid_Amount": []
#}

#name_list = []
#amount_list= []
#while (to_continue != 'no'):
#  name = input("What is your name?: ")
#  name_list.append(name)
#  amount = int(input("What's your Bid?: $"))
#  amount_list.append(amount)
#  to_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
#  clear()
  
#bidding_dict["Bidders"]= name_list
#bidding_dict["Bid_Amount"]= amount_list
#print(bidding_dict)
#bidding_dict["Bid_Amount"].sort()
#print(bidding_dict)

bidding_dict = {}



def check_bid(bidding_record):
  highest_bidder = ' '
  highest_bid = 0
  
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      highest_bidder = bidder
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

while (to_continue != 'no'):
  name = input("What is your name?: ")
  amount = int(input("What's your Bid?: $"))
  bidding_dict[name] = amount
  to_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  clear()

check_bid(bidding_dict)



