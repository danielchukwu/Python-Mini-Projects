# Python - 3.10
# Topic - Blind Auction
# Program - Write a program called blind auction, where multiple people get to bid for an item and the highest bidder wins the auction

# Expectations When ran=
# Welcome to the secret auction program.
# What's your name?: Angela
# What's your bid?: $53
# Are there any other bidders? Type 'yes' or 'no'.
# yes

# What's your name?: James
# What's your bid?: $34
# Are there any other bidders? Type 'yes' or 'no'.
# yes

# What's your name?: Michael
# What's your bid?: $121
# Are there any other bidders? Type 'yes' or 'no'.
# no

# The winner is Michael with a bid of $121.


# solution 👇✅
import os
import logo

print(logo.logo)
print("Welcome to the secret auction program.")

bidders = dict()

def place_bid():
   # get bidders name and bid
   name = input("What's your name?: ")
   bid = int( input("What's your bid?: $") )

   # add bid to dictionary
   bidders[name] = bid

def find_highest_bid():
   highest_bidder = ''
   highest_bid = 0
   for name in bidders:
      if bidders[name] > highest_bid:
         highest_bidder = name
         highest_bid = bidders[name]

   return highest_bidder, highest_bid

stop = False
while not stop:
   # place bid
   place_bid()
   # bid again or not
   option = input("Are there any other bidders? Type 'yes' or 'no'. \n")
   if option == 'yes':
      os.system('cls')
      continue
   stop = True


name, bid = find_highest_bid()
print(f"The winner is {name} with a bid of ${bid}.")