import time

from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()

cars = CarManager()

game_is_on = True

screen.listen()
screen.onkey(player.move, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    if player.is_at_finish_line():
        player.go_to_start()

    for car in cars.all_cars:
        if car.distance(player)<20:
            game_is_on = False

screen.exitonclick()