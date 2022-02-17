#this code is made to run on reeborg.ca
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# turn_right()

def turn_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()


turn_square()