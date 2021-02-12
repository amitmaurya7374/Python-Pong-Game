"""This class create a paddle and responsible of moving paddle when key is pressed"""
from turtle import Turtle


class Paddle(Turtle):
    """This class will create a paddle """

    def __init__(self):
        super().__init__()
        self.goto(x=350, y=0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.color("white")
        self.penup()
