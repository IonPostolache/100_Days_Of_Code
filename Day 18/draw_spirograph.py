from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
tim = Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.color("blue")
tim.speed(15)

rotation = 5
angle = 360
while angle > 0:
    tim.circle(100)
    tim.color(random_color())
    tim.left(rotation)
    angle = angle-rotation


screen.exitonclick()

