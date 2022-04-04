from art import logo
from art import vs
import random
from game_data import data

score=0
print(logo)
#print(f"Compare A: {A}.")
print(vs)
#print(f"Against B: {B}")

"""answer=input("Who has more followers? Type 'A' or 'B': ")
if answer=="A" and A.follower_count>B.follower_count:
    print(f"You're right! Current score: {score}.")
elif answer=="B" and A.follower_count<B.follower_count:
    print(f"You're right! Current score: {score}.")
elif answer=="A" and A.follower_count<B.follower_count:
    print(f"Sorry, that's wrong. Final score: {score}")
elif answer == "B" and A.follower_count > B.follower_count:
    print(f"Sorry, that's wrong. Final score: {score}")"""


#for i in range(len(data)):
    #print(i)

A=random.randint(1,len(data))
print(A)
print(len(data))


#create random A and random B from game_data
#check if the answer is correct or not
#make a loop that ends when an answer is wrong.
#make the score to increase or decrease
#At the 2nd question B becomes A
#create a function that includes all the answers
#create a function that selects a random A only forst time
#create a function that selects a random B every time
#create a function that extracts the follower_count
