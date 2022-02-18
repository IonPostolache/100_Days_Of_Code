#this code is made to run on reeborg.ca/Hurdle 1

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for a in range(0, 6):
    jump()
