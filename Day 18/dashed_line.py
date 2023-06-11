from turtle import Turtle, Screen


def dashed_line():
    tom.penup()
    tom.forward(5)
    tom.pendown()
    tom.forward(5)


screen = Screen()
tom = Turtle()
tom.color("blue")

for i in range(10):
    dashed_line()

tom.penup()
tom.forward(100)
tom.pendown()
tom.forward(100)


screen.exitonclick()
