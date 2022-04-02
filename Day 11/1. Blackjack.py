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
    comp_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))

    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")

    comp_flag=False
    if 10 in comp_cards and 11 in comp_cards:
        comp_flag=True

    user_flag=False
    if 10 in your_cards and 11 in your_cards:
        user_flag=True

    if comp_flag==False and user_flag==False:
        while sum(your_cards)<=21:
            get_card=input("Type 'y' to get another card, type 'n' to pass: ")
            if get_card=="y":
                another_card=random.choice(cards)
                your_cards.append(another_card)
                print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
                print(f"Computer's first card: {comp_cards}")
            elif get_card=="n":
                break

            if sum(your_cards) > 21:
                for l in range(len(your_cards)):
                    if your_cards[l]==11:
                        your_cards[l]=1

        while sum(comp_cards) < 17:
            comp_cards.append(random.choice(cards))
            if sum(comp_cards) >= 17:
                break

    print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
    print(f"Computer's final card: {comp_cards}, final score: {sum(comp_cards)}")

    if comp_flag==True:
        print("Lose, opponent has Blackjack 😱")
    elif user_flag==True and comp_flag==False:
        print("You win, you have Blackjack 😁")
    elif sum(your_cards)>21:
        print("You went over. You lose 😤")
    elif sum(your_cards)<=21 and sum(comp_cards)>21:
        print("Opponent went over. You win 😁")
    elif sum(comp_cards)<=21 and sum(your_cards)<sum(comp_cards):
        print("You lose 😤")
    elif sum(comp_cards) <= 21 and sum(your_cards) == sum(comp_cards):
        print("It's a draw")
    elif sum(your_cards) <= 21 and sum(your_cards) > sum(comp_cards):
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
