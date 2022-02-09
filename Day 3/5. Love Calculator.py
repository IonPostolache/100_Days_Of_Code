"""
Instructions
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5
L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3
Love Score = 53
Print: "Your score is 53."
Example Input 1
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1
Your score is 42, you are alright together.
Example Input 2
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
Example Output 2
Your score is 73.
e.g. When you hit run, this is what should happen:
https://cdn.fs.teachablecdn.com/nfSILIPSNaIOwWhPR5vr
The testing code will check for print output that is formatted like one of the lines below:
"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."
Hint
The lower() function changes all the letters in a string to lower case.
https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python
The count() function will give you the number of times a letter occurs in a string.
https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string
"""
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lname1=name1.lower()
lname2=name2.lower()
Trueword1=lname1.count("t")+lname1.count("r")+lname1.count("u")+lname1.count("e")
Trueword2=lname2.count("t")+lname2.count("r")+lname2.count("u")+lname2.count("e")
Truew=Trueword1+Trueword2
loveword1=lname1.count("l")+lname1.count("o")+lname1.count("v")+lname1.count("e")
loveword2=lname2.count("l")+lname2.count("o")+lname2.count("v")+lname2.count("e")
lovew=loveword1+loveword2
lovescore=Truew+lovew

if lovescore<10 or lovescore>90:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore>=40 and lovescore<=50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")