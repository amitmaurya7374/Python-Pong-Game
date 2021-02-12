"""In This project we will created pong game."""
from turtle import Screen

from paddle import Paddle

# Screen setup
screen = Screen()  # created an object
screen.bgcolor("black")  # set a black color to a screen
screen.title("Pong Game")  # set a title on gui
screen.setup(width=800, height=600)  # set a height and width of a GUI

paddle = Paddle()
screen.listen()
print(paddle.heading())

screen.onkey(key="Up", fun=paddle.move_upwards)
screen.onkey(key="Down",fun=paddle.move_downwards)
screen.exitonclick()
