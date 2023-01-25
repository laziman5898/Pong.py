from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.current_speed =0.05
        self.speedy = 10
        self.speedx = 10

    def update(self):
       new_position = (self.xcor()+self.speedx,self.ycor()+self.speedy)
       self.goto(new_position)

    def reverse_y_direction(self):
        self.speedy *=-1

    def reverse_x_direction(self):
        self.speedx *= -1
        self.current_speed*=0.5

    def restart(self):
        self.goto(0,0)
        self.current_speed = 0.05


