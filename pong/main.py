from turtle import Screen
from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle1()
paddle2 = Paddle2()
ball = Ball()
scoreboard = ScoreBoard()

game_is_on = True

screen.listen()
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")

screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()
    
    if ball.distance(paddle1.segments[1]) < 50 and ball.xcor() < -350:
        ball.bounce_x()
        scoreboard.left_point()
        time.sleep(0.1)

    if ball.distance(paddle2.segments[1]) < 50 and ball.xcor() > 350:
        ball.bounce_x()
        scoreboard.right_point()
        time.sleep(0.1)

    if ball.xcor() > 390 or ball.xcor() < -390:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()