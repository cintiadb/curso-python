
#from replit import clear
#HINT: You can call clear() to clear the output in the console

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  

def find_highest_bidder(bidding_record):
  highest_bid = 100
  winner = ""
  # bidding_record = {"Angela": 1, "James": 521, "Cintia": 500}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]

    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder

    # if bidding_record[bidder] > highest_bid: 
    #   highest_bid = bidding_record[bidder]
    #   winner = bidder

  print(f"The winner is {winner} with a bid of ${highest_bid}")


logo = '''
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
                      
'''

print(logo)

bids = {}
bidding_finished = False

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  # Guardamos bidder y su bid price en el diccionario
  # Si el nombre del bidder no existe, lo crea. 
  # Si existe, lo actualiza.
  # { "_nombre_": _precio_ } -> { str(bidder): int(price) } -> { key: value } 
  bids[name] = price

  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()