from art import logo
import random
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    print(logo)
    your_cards = []
    comp_cards = []
    your_cards.append(random.choice(cards))
    your_cards.append(random.choice(cards))
    current_score = 0
    for i in your_cards:
        current_score+=i
    print(f"Your cards: {your_cards}, current score: {current_score}")
    comp_cards.append(random.choice(cards))
    print(f"Computer's first card: {comp_cards}")

    while current_score<=21:
        get_card=input("Type 'y' to get another card, type 'n' to pass: ")
        if get_card=="y":
            another_card=random.choice(cards)
            your_cards.append(another_card)
            current_score += another_card
            print(f"Your cards: {your_cards}, current score: {current_score}")
            print(f"Computer's first card: {comp_cards}")
        elif get_card=="n":
            break

    print(f"Your final hand: {your_cards}, final score: {current_score}")
    comp_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))
    comp_score = 0
    for j in comp_cards:
        comp_score+=j
    print(f"Computer's final card: {comp_cards}, final score: {comp_score}")
    if current_score>21:
        print("You went over. You lose 😤")
    elif current_score<=21 and comp_score>21:
        print("Opponent went over. You win 😁")
    elif comp_score<=21 and current_score<comp_score:
        print("You lose 😤")
    elif current_score <= 21 and current_score > comp_score:
        print("You win 😃")


    continuation2=input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if continuation2=="n":
        return
    elif continuation2=="y":
        blackjack()


start = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start == "y":
    blackjack()




##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run
