#this code is made to run on reeborg.ca/maze
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def right():
    for m in range(0, 5):
        if right_is_clear():
            turn_right()
            move()
        m -= 1
    if front_is_clear():
        move()

def go():
    if right_is_clear():
        right()
    elif front_is_clear():
        move()
    else:
        turn_left()

while not at_goal():
    go()
