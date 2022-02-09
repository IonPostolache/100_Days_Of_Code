print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
price=0
if height>=120:
    print(("Can ride"))
    age=int(input("What is your age?"))
    if age<12:
        price=5
    elif age <18:
        price=7
    else:
        price=12
    print(f"Ticket price is {price}")

else:
    print("Can't ride")

photos=input("Do you want photos? ")
if photos=="yes":
    print(f"The total bill is {price+3}")
elif photos=="no":
    print(f"The total bill is {price}")



