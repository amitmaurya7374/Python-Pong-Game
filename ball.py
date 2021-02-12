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
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """This function is responsible for movement of ball"""
        x_coordinate = self.xcor() + self.x_move
        y_coordinate = self.ycor() + self.y_move
        self.goto(x_coordinate, y_coordinate)

    def bounce(self):
        """This function help a ball to bounce"""
        self.y_move *= -1

