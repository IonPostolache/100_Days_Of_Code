# import turtle
from turtle import Turtle, Screen

# timmy=turtle.Turtle()
tomitza = Turtle()
print(tomitza)
tomitza.shape("turtle")
tomitza.color("coral")
tomitza.forward(200)
tomitza.back(100)

my_screen = Screen()
print(my_screen.canvheight)
# turtle.color("Darkred")
my_screen.exitonclick()

# import prettytable
from prettytable import PrettyTable

table = PrettyTable()
# table.add_column(fieldname="name", column=1)
# print(table)
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], align="l")
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
table.min_table_width = 60
print(table)




