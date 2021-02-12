"""This class create a paddle and responsible of moving paddle when key is pressed"""
from turtle import Turtle


class Paddle(Turtle):
    """This class will create a paddle """

    def __init__(self, paddle_position):
        super().__init__()
        self.goto(paddle_position)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.color("white")
        self.penup()

    def move_upwards(self):
        """Move Paddle Upward Direction"""
        new_y_coordinate = self.ycor() + 20  # return a y_coordinate and add 20 in it
        self.goto(self.xcor(), new_y_coordinate)

    def move_downwards(self):
        """Move Paddle Downward Direction"""
        new_y_coordinate = self.ycor() - 20
        self.goto(self.xcor(), new_y_coordinate)
