print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height>=120:
    print(("Can ride"))
    age=int(input("What is your age?"))
    if age<12:
        print("Ticket price is 5")
    elif age <18:
        print("Ticket price is 7")
    else:
        print("Ticket price is 12")
else:
    print("Can't ride")