#from replit import clear
#HINT: You can call clear() to clear the output in the console.
#replit only works on replit website?
import os
from time import sleep

from art import logo
print(logo)

all_bidders_dict={}
flag=True
counter = 0

while flag==True:
    bidder_name=input("What is your name?")
    bid_price=input("What is your bid price?")
    all_bidders_dict[bidder_name]=bid_price
    #print(all_bidders_dict)

    more_users=input("Are there other users who want to bid? 'yes' or 'no'.")
    if more_users=="yes":
        os.system('clear')  # on linux / os x
        print("\033[H\033[J")
        #clear()
        continue
    elif more_users=="no":
        max_key=max(all_bidders_dict, key=all_bidders_dict.get)
        print(f"The winner is: {max_key}")
        flag=False
