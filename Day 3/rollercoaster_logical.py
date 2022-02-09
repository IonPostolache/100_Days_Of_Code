print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
price=0
if height>=120:
    print(("Can ride"))
    age=int(input("What is your age?"))
    if age<12:
        price=5
    elif age<18:
        price=7
    elif age<55 and age>45:
        price=0
    else:
        price=12
    print(f"Ticket price is {price}")
    photos = input("Do you want photos? Y or N")
    if photos == "Y":
        price+=3
    print(f"The total bill is {price}")

else:
    print("Can't ride")