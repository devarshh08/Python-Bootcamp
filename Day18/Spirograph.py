from turtle import Turtle, Screen
import random

colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]

timmy = Turtle()

for _ in range(100):
    timmy.color(random.choice(colours))
    timmy.circle(100)
    timmy.tilt(50)
    timmy.right(8)
    timmy.speed('fastest')

screen = Screen()
screen.exitonclick()
