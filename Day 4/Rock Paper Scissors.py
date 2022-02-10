"""Instructions
Make a rock, paper, scissors game.
Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable:
rock, paper, and scissors. This will make it easy to print them out to the console.
Start the game by asking the player:
"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
From there you will need to figure out:
How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player."""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
options=["Rock", "Paper", "Scissors"]
human_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if human_choice<=0 or human_choice>2:
    print("You typed an invalid choice. You lost!")
else:
    print(f"Your choice is {options[human_choice]}.")
    #generate a random choice for the computer
    computer_choice=random.randint(0,2)
    print(f"Computer choice is {options[computer_choice]}.")
    #rules:
    # Rock wins against scissors.
    # Scissors win against paper.
    # Paper wins against rock.
    if human_choice==0 and computer_choice==2:
        print("You won!")
    elif human_choice==2 and computer_choice==0:
        print("You lost!")
    elif human_choice==2 and computer_choice==1:
        print("You won!")
    elif human_choice==1 and computer_choice==2:
        print("You lost!")
    elif human_choice==1 and computer_choice==0:
        print("You won!")
    elif human_choice==0 and computer_choice==1:
        print("You lost!")
    elif human_choice==computer_choice:
        print("It's a draw!")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end