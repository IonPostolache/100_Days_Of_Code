from turtle import Turtle, Screen

screen = Screen()

tomy_turtle = Turtle()
tomy_turtle.color("red")
tomy_turtle.shape("turtle")

for i in range(4):
    tomy_turtle.forward(100)
    tomy_turtle.right(90)

screen.exitonclick()
