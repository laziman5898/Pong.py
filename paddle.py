from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, posx, posy, player):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.player_no = player
        self.pos_x=posx
        self.pos_y = posy
        self.goto(posx, posy)

    def moveUp(self):
        if self.pos_y<350:
            self.pos_y+=20
            self.goto(self.pos_x,self.pos_y)

    def moveDown(self):
        if self.pos_y > -350:
            self.pos_y-=20
            self.goto(self.pos_x,self.pos_y)



