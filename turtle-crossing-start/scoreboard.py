from turtle import Turtle
FONT = ("Courier", 24, "normal")
POSITION = (-200, 260)
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(POSITION)
        self.write(f"SCORE = {self.score}", align="center", font=(FONT))

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(POSITION)
        self.write(f"               GAME OVER final score = {self.score}", align="center", font=(FONT))
