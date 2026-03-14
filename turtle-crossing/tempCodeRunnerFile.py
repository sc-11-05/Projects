from turtle import Screen
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()

game_is_on = True

screen.listen()
screen.onkey(player.move, "Up")

while game_is_on:
    screen.update()

screen.exitonclick()