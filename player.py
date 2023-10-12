import random
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Player(Turtle):

    def __init__(self):
        super().__init__()
        random_index = random.randint(0, 5)
        self.color(COLORS[random_index])
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)
