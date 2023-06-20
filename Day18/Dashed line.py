from turtle import Turtle, Screen

timmy = Turtle()

for i in range(20):
    timmy.fd(4)
    timmy.penup()
    timmy.fd(4)
    timmy.pendown()

screen = Screen()
screen.exitonclick()