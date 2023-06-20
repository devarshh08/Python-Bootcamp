import colorgram
from turtle import Turtle, Screen
import random

timmy = Turtle()
colours = colorgram.extract("E:\\CODING\\100 Days Of Code\\100-Days-of-Code\\Day18\\image.png", 30)

rgb_colours = []
for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    new_colour = (r, g, b)
    rgb_colours.append(new_colour)

colour_list = list(rgb_colours)

timmy.pu()
timmy.setx(-250)
timmy.sety(-220)
timmy.pd()

screen = Screen()
screen.colormode(255)
timmy.speed('fast')

for _ in range(10):
    color_choice = random.choice(colour_list)
    timmy.pencolor(color_choice)
    for _ in range(10):
        color_choice = random.choice(colour_list)
        timmy.pencolor(color_choice)
        timmy.dot(20)
        timmy.pu()
        timmy.setheading(360)
        timmy.fd(50)
        timmy.pd()
    timmy.pu()
    timmy.setheading(90)
    timmy.fd(50)
    timmy.setheading(180)
    timmy.fd(500)
    timmy.pd()

screen.exitonclick()
