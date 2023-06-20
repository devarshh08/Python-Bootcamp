from turtle import Turtle, Screen
import random

colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]

timmy = Turtle()

for num_sides in range(3,11):
    angle = 360/num_sides
    colourr = random.choice(colours)
    for _ in range(num_sides):
        timmy.color(colourr)
        timmy.fd(100)
        timmy.right(angle)

screen = Screen()
screen.exitonclick()