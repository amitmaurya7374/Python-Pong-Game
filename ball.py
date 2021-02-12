"""In this class we create a blueprint of a ball"""

from turtle import Turtle


class Ball(Turtle):
    """This class creates a ball and handle all moving Operations"""

    def __init__(self):
        """Initial setting of ball"""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.goto(x=0, y=0)
        self.penup()

    def move(self):
        """This function is responsible for movement of ball"""
        x_coordinate = self.xcor() + 10
        y_coordinate = self.ycor() + 10
        self.goto(x_coordinate, y_coordinate)
