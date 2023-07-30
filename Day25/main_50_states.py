import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "E:/CODING/GitHub Repositories/100-Days-of-Code/Day25/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title = "Guess the state: ", prompt = "What's another state's name?")

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop() #similar to exitonclick
