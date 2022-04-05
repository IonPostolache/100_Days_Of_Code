from art import logo
from art import vs
import random
from game_data import data

print(logo)
print(f"Compare A: {data[1]['name']}, a {data[1]['description']}, from {data[1]['country']}.")
print(vs)
print(f"Against B: {data[2]['name']}, a {data[2]['description']}, from {data[2]['country']}.")

score=0
def scoring(increment):
    score=score+increment
    return score


def check():
    selection=input("Who has more followers? Type 'A' or 'B': ")
    if selection=="A" and data[1]['follower_count']>data[2]['follower_count']:
        scoring(-1)
        print(f"You're right! Current score: {score}.")
    elif selection=="B" and data[1]['follower_count']<data[2]['follower_count']:
        print(f"You're right! Current score: {score}.")
    elif selection=="A" and data[1]['follower_count']<data[2]['follower_count']:
        print(f"Sorry, that's wrong. Final score: {score}")
    elif selection == "B" and data[1]['follower_count'] > data[2]['follower_count']:
        print(f"Sorry, that's wrong. Final score: {score}")
check()



#for i in range(len(data)):
    #print(i)

def random_generator():
    generated = random.randint(0, len(data) - 1)
    return generated

#test function
test_list=["a", "b", "c", "d"]
A=random.randint(0,len(test_list)-1)
print(f"random number is {A}")
print(f"length of the list is: {len(test_list)}")
print(f"element from the list corresponding to random index: {test_list[A]}")

print(data[0])
print(data[0]['name'])

#create random A and random B from game_data
#check if the answer is correct or not
#make a loop that ends when an answer is wrong.
#make the score to increase or decrease
#At the 2nd question B becomes A
#create a function that includes all the answers
#create a function that selects a random A only forst time
#create a function that selects a random B every time
#create a function that extracts the follower_count
