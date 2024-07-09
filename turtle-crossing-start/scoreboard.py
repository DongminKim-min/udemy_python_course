from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def show_score(self, current_level):
        self.clear()
        self.goto(-200, 250)
        self.write(arg=f"Level: {current_level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(arg="GAME OVER", align="center", font=FONT)