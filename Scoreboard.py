from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200,310)
        self.Lscore = 0
        self.Rscore = 0
        self.color("white")
        self.write(f"{self.Lscore}" , align="center" , font=("Courier" , 50, "normal"))
        self.goto(200, 310)
        self.write(f"{self.Rscore}", align="center", font=("Courier", 50, "normal"))

    def update_score_right(self):
        self.Rscore += 1
        self.clear()
        self.goto(-200, 310)
        self.write(f"{self.Lscore}", align="center", font=("Courier", 50, "normal"))
        self.goto(200, 310)
        self.write(f"{self.Rscore}", align="center", font=("Courier", 50, "normal"))

    def update_score_left(self):
        self.Lscore += 1
        self.clear()
        self.goto(-200, 310)
        self.write(f"{self.Lscore}", align="center", font=("Courier", 50, "normal"))
        self.goto(200, 310)
        self.write(f"{self.Rscore}", align="center", font=("Courier", 50, "normal"))
