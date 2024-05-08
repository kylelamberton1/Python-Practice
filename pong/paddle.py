from turtle import Turtle

DISTANCE = 20
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.setpos(position)
        self.color("white")


    def up(self):
        new_pos = self.ycor() + DISTANCE
        self.goto(self.xcor(), new_pos)

    def down(self):
        new_pos = self.ycor() - DISTANCE
        self.goto(self.xcor(), new_pos)
