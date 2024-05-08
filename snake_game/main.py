from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakey")
screen.tracer(0)


########## MY SOLUTION ############

# x_positions = [0, -20, -40]
# for turtle_index in range(0, 3):
#     new_t = Turtle()
#     new_t.shape("square")
#     new_t.color("white")
#     new_t.goto(x=x_positions[turtle_index], y=0)

########### HER SOLUTION ##########

# staring_positions = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
# for position in staring_positions:
#     new_t = Turtle("square")
#     new_t.color("white")
#     new_t.penup()
#     new_t.goto(position)
#     segments.append(new_t)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    #for seg_num in range(start=2, stop=0, step=-1):  ### range function does not read keywords so need to delete ###
    # for seg_num in range(len(segments)-1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)

    snake.move()

    ##DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.change_score()

    ##DETECT COLLISION WITH WALL
    if snake.head.xcor() > 290 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    ##DETECT COLLISION WITH TAIL
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()