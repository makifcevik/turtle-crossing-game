import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(key="Up", fun=player.move)

cars = []
current_time = time.time()


def spawn_car():
    global current_time
    if time.time() - 0.3 > current_time:
        current_time = time.time()
        new_car = CarManager()
        cars.append(new_car)
    for car in cars:
        car.move()


game_is_on = True
while game_is_on:
    time.sleep(0.040)
    spawn_car()
    screen.update()

screen.exitonclick()
