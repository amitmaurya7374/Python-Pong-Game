"""In This project we will created pong game."""
from turtle import Screen

from paddle import Paddle

# Screen setup
screen = Screen()  # created an object
screen.bgcolor("black")  # set a black color to a screen
screen.title("Pong Game")  # set a title on gui
screen.setup(width=800, height=600)  # set a height and width of a GUI
screen.tracer(0)  # turning off a screen animation

right_paddle = Paddle(paddle_position=(350, 0))

left_paddle = Paddle(paddle_position=(-350, 0))  # created second paddle for second player

screen.listen()


def move_paddle(key1, key2, function1, function2):
    """Move paddle when key pressed.\n
    This is a high order function => passing function as argument inside another
    function """
    screen.onkey(key=key1, fun=function1)
    screen.onkey(key=key2, fun=function2)


move_paddle(key1="Up", key2="Down", function1=right_paddle.move_upwards, function2=right_paddle.move_downwards)
move_paddle(key1="Left", key2="Right", function1=left_paddle.move_upwards, function2=left_paddle.move_downwards)

is_game_on = True

while is_game_on:
    screen.update()

screen.exitonclick()
