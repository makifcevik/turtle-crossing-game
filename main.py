import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

GAME_TICK = 0.040
WIN_PAUSE_DURATION = 1.5
SPAWN_TIME = 0.25

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(key="Up", fun=player.move)

cars = []
current_time = time.time()
level = 1


def spawn_car(speed_level):
    global current_time
    if time.time() - SPAWN_TIME > current_time:
        current_time = time.time()
        new_car = CarManager(speed_level)
        cars.append(new_car)
    for car in cars:
        car.move()


def check_win():
    global level
    if player.ycor() > 280:
        level += 1
        for car in cars:
            car.remove_car()
        cars.clear()
        player.goto((0, -280))
        screen.update()
        time.sleep(WIN_PAUSE_DURATION)


game_is_on = True
while game_is_on:
    time.sleep(GAME_TICK)
    spawn_car(level)
    check_win()
    screen.update()

screen.exitonclick()
