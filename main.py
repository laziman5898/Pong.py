from turtle import Screen
from Scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

canvas = Screen()
canvas.screensize(500, 500)
canvas.bgcolor("black")
canvas.title("Pong")
canvas.tracer(0)
player1 = Paddle(posx=-350, posy=0, player="Player1")
player2 = Paddle(posx=350, posy=0, player="Player2")
ball = Ball()
scoreboard = Scoreboard()
game_state = True

canvas.listen()
canvas.onkeypress(key="Up", fun=player1.moveUp)
canvas.onkeypress(key="Down", fun=player1.moveDown)
canvas.onkeypress(key="w", fun=player2.moveUp)
canvas.onkeypress(key="s", fun=player2.moveDown)

while game_state:
    canvas.update()
    ball.update()

    if ball.ycor() == 400 or ball.ycor() == -400:
        ball.reverse_y_direction()
    if ball.distance(player2) < 50 and ball.xcor() > 330:
        ball.reverse_x_direction()
    if ball.distance(player1) < 50 and ball.xcor() < -330:
        ball.reverse_x_direction()

    if ball.xcor() > 400:
        ball.restart()
        scoreboard.update_score_left()
    elif ball.xcor() < -400:
        ball.restart()
        scoreboard.update_score_right()

    time.sleep(ball.current_speed)

canvas.exitonclick()
