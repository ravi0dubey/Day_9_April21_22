from replit import clear
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
  amount = int(input("What's your Bid?: $"))
  amount_list.append(amount)
  to_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  clear()
  
bidding_dict["Bidders"]= name_list
bidding_dict["Bid_Amount"]= amount_list

print(bidding_dict)
bidding_dict["Bid_Amount"].sort()
print(bidding_dict)
len1 =len(bidding_dict["Bid_Amount"])
high_bid_amount = bidding_dict["Bid_Amount"][len1-1]

print(f"The winner is {name} with a bid of ${high_bid_amount}")