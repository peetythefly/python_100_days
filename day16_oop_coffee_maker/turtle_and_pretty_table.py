import turtle
from turtle import Turtle, Screen
# timmy = turtle.Turtle()
ninja = Turtle()
my_screen = Screen()
ninja.shape("turtle")
ninja.color("green4")
# print(ninja)
print(my_screen.canvheight)
print(ninja.position())
for iterator in range(4):
    ninja.forward(200)
    ninja.right(90)
ninja.back(100)
ninja.right(720)
ninja.shape("circle")
# print(ninja)
my_screen.exitonclick()
print(ninja.position())

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]

table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "l"

print(table)