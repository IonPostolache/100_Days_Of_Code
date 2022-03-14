#from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

all_bidders_dict={}
flag=True
counter = 0

while flag==True:
    bidder_name=input("What is your name?")
    bid_price=input("What is your bid price?")
    all_bidders_dict[bidder_name]=bid_price
    print(all_bidders_dict)

    more_users=input("Are there other users who want to bid? 'yes' or 'no'.")
    if more_users=="yes":
        #clear the screen
        #clear()
        continue
    elif more_users=="no":
        #find the highest bid in the dictionary and declare them as a winner.
        for key, value in all_bidders_dict.items():
            #if int(value)>int(counter):
            if int(all_bidders_dict[key])>counter:
                counter=all_bidders_dict[value]

                #counter=value
        print(value[counter])
        print(f"The winner is: {counter}")
        flag=False


