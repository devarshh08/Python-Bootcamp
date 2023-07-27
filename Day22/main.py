from turtle import Turtle, Screen
from paddle import Paddle

timmy = Turtle()
screen = Screen()

screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.exitonclick()

paddle = Paddle()