from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score} ", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=("Arial", 40, "normal"))
    def change_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()









