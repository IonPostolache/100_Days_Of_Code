# draw a triangle, square, .... decagon.

from turtle import Turtle, Screen
import random

screen = Screen()
tom = Turtle()


def create_shape(number_of_sides):
    angle = 360/number_of_sides
    for j in range(number_of_sides):
        tom.forward(100)
        tom.right(angle)


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


for i in range(3, 11):
    tom.color(random_color())
    create_shape(i)

screen.exitonclick()
