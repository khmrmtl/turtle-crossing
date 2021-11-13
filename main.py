import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

difficulty = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")
screen.listen()

game_is_on = True
while game_is_on:

    if random.randint(0, difficulty) == 1:
        car = CarManager()

    if player.check_finish():
        if difficulty != 1:
            difficulty -= 1
        CarManager.increase_speed()
        scoreboard.print_level()

    for car in CarManager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    CarManager.move()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
