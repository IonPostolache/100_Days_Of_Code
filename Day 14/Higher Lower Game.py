from art import logo
from art import vs
import random
from game_data import data


def random_generator():
    """generates a random number in the data len range"""
    generated = random.randint(0, len(data) - 1)
    return generated


ran_A=random_generator()
ran_B=random_generator()


flag=True
def play():
    """function to play Higher Lower game"""
    print(logo)
    new_score=0
    temp_ran_A=ran_A
    while flag==True:
        ran_B=random_generator()
        print(f"Compare A: {data[temp_ran_A]['name']}, a {data[temp_ran_A]['description']}, from {data[temp_ran_A]['country']}.")
        print(vs)
        print(f"Against B: {data[ran_B]['name']}, a {data[ran_B]['description']}, from {data[ran_B]['country']}.")
        selection=input("Who has more followers? Type 'A' or 'B': ")
        print(logo)
        if (selection == "A" and data[temp_ran_A]['follower_count'] > data[ran_B]['follower_count']) or \
                (selection == "B" and data[temp_ran_A]['follower_count'] < data[ran_B]['follower_count']):
            new_score += 1
            print(f"You're right! Current score: {new_score}.")
        elif (selection == "A" and data[temp_ran_A]['follower_count'] < data[ran_B]['follower_count']) or \
                (selection == "B" and data[temp_ran_A]['follower_count'] > data[ran_B]['follower_count']):
            new_score -= 1
            if new_score<0:
                new_score=0
            print(f"Sorry, that's wrong. Final score: {new_score}")
            break
        temp_ran_A=ran_B

play()

