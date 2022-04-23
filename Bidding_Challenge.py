print("Welcome to the secret auction program.\n")
to_continue = "Yes"
bidding_dict = {
  
#  "Bidders":[ "Farzi",],
#  "Bid_Amount": [0,]
  "Bidders":[ ],
  "Bid_Amount": []
  
}

name_list = []
amount_list= []
while (to_continue != 'no'):
  name = input("What is your name?: ")
  name_list.append(name)
  bid_amount = int(input("What's your Bid?: $"))
  amount_list.append(bid_amount)
  to_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

  
bidding_dict["Bidders"]= name_list
bidding_dict["Bid_Amount"]= amount_list

print(bidding_dict)
#print(bidding_dict["Bid_amount"].sort())


#print(f"The winner is {name} with a bid of ${bid_amount}")