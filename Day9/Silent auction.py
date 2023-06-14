from replit import clear

bidding_finished = False
bid_details = {}

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
def bidding_winner(bid_details):
  highest_amount = 0
  for name in bid_details:
    bidding_amount = bid_details[name]
    if bidding_amount > highest_amount:
      highest_amount = bidding_amount
      winner = name
  clear()

  print(f"Auction winner is {name} with a bid of {highest_amount}")



while bidding_finished == False:
  name = input("What is your name?\n")
  amount = int(input("What is your bid amount?\n"))
  bid_details[name] = amount
  continue_bid = input("Are there other bidders? yes or no? \n")
  if continue_bid == "no":
    bidding_finished = True
  elif continue_bid == "yes":
    clear()
  else:
    print("Please enter a valid choice and restart")
    bidding_finished == True
    
bidding_winner(bid_details)
  