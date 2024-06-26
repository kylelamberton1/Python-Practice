from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def move_turtle(self):
        new_pos = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_pos)


    def finish_line(self):
        if self.ycor() + MOVE_DISTANCE == FINISH_LINE_Y:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(0, -280)





