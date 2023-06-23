from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.fd(10)

def move_backward():
    tim.bk(10)

def clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def counterclockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()

def home():
    tim.pu()
    tim.home()
    tim.pd()

screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_forward)
screen.onkey(key = "a", fun = counterclockwise)
screen.onkey(key = "d", fun = clockwise)
screen.onkey(key = "h", fun = home)
screen.onkey(key = "BackSpace", fun = clear)
screen.exitonclick()



