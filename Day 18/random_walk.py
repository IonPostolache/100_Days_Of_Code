# random walk, same distance but random direction, random colors, thicker lines, speedup the turtle
import random
from turtle import Turtle, Screen

directions = [-90, 90, 0, 180]

screen = Screen()
tim = Turtle()


tim.color("blue")
tim.width(15)
tim.speed(8)


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


move = 0
moves = 50
while move < moves:
    direction = random.choice(directions)
    tim.color(random_color())

    tim.forward(30)
    tim.right(direction)
    move += 1

screen.exitonclick()
