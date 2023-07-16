from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0, 260)
        self.pd()
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.pu()
        self.goto(0, 0)
        self.pd()
        self.color("white")
        self.write("GAME OVER", align = "center", font = ("Arial", 27, "normal"))