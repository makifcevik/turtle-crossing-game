from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.goto(-290, 260)

        self.update()

    def update(self, level: int = 1):
        self.clear()
        self.write(arg=f"Level: {level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(arg="GAME OVER", align="center", font=FONT)

