from art import logo
from art import vs
import random
from game_data import data


def random_generator():
    """generates a random number in the data len range"""
    generated = random.randint(0, len(data) - 1)
    return generated


ran_a = random_generator()
ran_b = random_generator()

flag = True


def play():
    """function to play Higher Lower game"""
    print(logo)
    new_score = 0
    t_ran_a = ran_a
    while flag:
        ran_b2 = random_generator()
        print(
            f"Compare A: {data[t_ran_a]['name']}, a {data[t_ran_a]['description']}, from {data[t_ran_a]['country']}.")
        print(vs)
        print(f"Against B: {data[ran_b2]['name']}, a {data[ran_b2]['description']}, from {data[ran_b2]['country']}.")
        selection = input("Who has more followers? Type 'A' or 'B': ")
        print(logo)
        if (selection == "A" and data[t_ran_a]['follower_count'] > data[ran_b2]['follower_count']) or \
                (selection == "B" and data[t_ran_a]['follower_count'] < data[ran_b2]['follower_count']):
            new_score += 1
            print(f"You're right! Current score: {new_score}.")
        elif (selection == "A" and data[t_ran_a]['follower_count'] < data[ran_b2]['follower_count']) or \
                (selection == "B" and data[t_ran_a]['follower_count'] > data[ran_b2]['follower_count']):
            new_score -= 1
            if new_score < 0:
                new_score = 0
            print(f"Sorry, that's wrong. Final score: {new_score}")
            break
        t_ran_a = ran_b2


play()
