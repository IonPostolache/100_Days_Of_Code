from art import logo
import random


print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
guessed_number=random.randint(1,100)
print(f"Pssst, the correct answer is {guessed_number}")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts=0
if difficulty == "easy":
    attempts =10
elif difficulty == "hard":
    attempts =5
call2=attempts
def guessing():
    attempts=call2
    while attempts>0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        current_try = int(input("Make a guess: "))
        if current_try==guessed_number:
            print(f"You got it! The answer was {guessed_number}.")
            break
        elif current_try < guessed_number:
            print("Too low.")
            print("Guess again.")
        elif current_try > guessed_number:
            print("Too high.")
            print("Guess again.")
        print(f"attempts {attempts}")
        attempts=attempts-1

        guessing()

guessing()



#make a guess several times----function??? or while loop?

#compare the guess with the number and print too high or too low

#count the number of attempts

#if guessing print the correct message

#if run out of guesses print the correct message



"""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Pssst, the correct answer is 8
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
hard
You have 5 attempts remaining to guess the number.
Make a guess: 50
Too high.
Guess again.
You have 9 attempts remaining to guess the number.
Make a guess: 25
Too high.
Guess again.
You have 8 attempts remaining to guess the number.
Make a guess: 35
Too high.
Guess again.

You've run out of guesses, you lose.
You got it! The answer was 54."""

