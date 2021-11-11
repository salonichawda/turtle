from turtle import*

setup()

tl=Turtle()

colors=["red","blue","green","yellow","purple","orange"]

import random

tl.up()

tl.goto(-200,0)

tl.down()

tl.width(6)

tl.hideturtle()

tl.speed(0)

for i in range(9001):
    colorchoice=random.choice(colors)

    tl.color(colorchoice)

    tl.forward(500)

    tl.right(185)