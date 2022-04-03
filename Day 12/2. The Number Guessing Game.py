from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
guessed_number=random.randint(1,100)
print(f"Pssst, the correct answer is {guessed_number}")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")


def difficulty_option():
    """This function will return the number of attempts"""
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    return attempts


def guessing():
    """Main function using a while loop to guess the number"""
    attempts_inside=difficulty_option()
    while attempts_inside>0:
        print(f"You have {attempts_inside} attempts remaining to guess the number.")
        attempts_inside-=1
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
        if attempts_inside==0:
            print("You've run out of guesses, you lose.")


guessing()
