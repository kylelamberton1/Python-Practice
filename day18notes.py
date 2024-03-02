from turtle import Turtle, Screen
from random import Random

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("lime green")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

import turtle as t

tim = t.Turtle()

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# triangle = 360 / 3
# square = 360 / 4
# pentagon = 360 / 5
# hexagon = 360 / 6
# heptagon = 360 / 7
# octagon = 360 / 8
# nonagon = 360 / 9
# decagon = 360 / 10
# for _ in range(3):
#     tim.color("blue")
#     tim.forward(50)
#     tim.right(triangle)
# for _ in range(4):
#     tim.color("green")
#     tim.forward(50)
#     tim.right(square)
# for _ in range(5):
#     tim.color("red")
#     tim.forward(50)
#     tim.right(pentagon)
# for _ in range(6):
#     tim.color("yellow")
#     tim.forward(50)
#     tim.right(hexagon)
# for _ in range(7):
#     tim.color("purple")
#     tim.forward(50)
#     tim.right(heptagon)
# for _ in range(8):
#     tim.color("orange")
#     tim.forward(50)
#     tim.right(octagon)
# for _ in range(9):
#     tim.color("pink")
#     tim.forward(50)
#     tim.right(nonagon)
# for _ in range(10):
#     tim.color("brown")
#     tim.forward(50)
#     tim.right(decagon)

import random

# colours = ["AntiqueWhite1", "DeepPink3", "GreenYellow", "LightCyan4", "OrangeRed", "salmon4", "seashell2", "VioletRed4"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)
# t.colormode(255)
# tim.shape("circle")
# tim.shapesize(0.5)
# tim.pensize(15)
#
# def random_colour():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     col_tuple = (r,g,b)
#     return col_tuple
#
# directions = [0, 90, 180, 270]
# tim.speed("fastest")
#
#
# for _ in range(1000):
#   tim.color(random_colour())
#   tim.forward(30)
#   tim.setheading(random.choice(directions))


t.colormode(255)
def random_colour():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    col_tuple = (r,g,b)
    return col_tuple

####### MY-WAY ########
# tim.speed("fastest")
# for _ in range(100):
#     tim.color(random_colour())
#     tim.circle(100)
#     tim.right(3.60)

####### HER-WAY #######
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range (int(360 / size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)












screen = t.Screen()
screen.exitonclick()
