from turtle import Turtle, Screen
import random

colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
directions = [0, 90, 180, 270]

timmy = Turtle()

for _ in range(200):
    timmy.pensize(10)
    timmy.color(random.choice(colours)) 
    timmy.fd(30)
    timmy.setheading(random.choice(directions))
    timmy.speed('fastest')

screen = Screen()
screen.exitonclick()