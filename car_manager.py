import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):

    def __init__(self, speed_level: int = 1):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)

        random_y = random.randint(-230, 230)
        self.goto(300, random_y)

        self.speed_level = speed_level

    def move(self):
        if self.xcor() > -300:
            self.setx(self.xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT * (self.speed_level - 1))
        else:
            self.remove_car()

    def remove_car(self):
        self.goto(-350, 0)
        self.hideturtle()
