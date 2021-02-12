"""In This project we will created pong game."""
import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from score import Score

# Screen setup
screen = Screen()  # created an object
screen.bgcolor("black")  # set a black color to a screen
screen.title("Pong Game")  # set a title on gui
screen.setup(width=800, height=600)  # set a height and width of a GUI
screen.tracer(0)  # turning off a screen animation

right_paddle = Paddle(paddle_position=(350, 0))

left_paddle = Paddle(paddle_position=(-350, 0))  # created second paddle for second player

ball = Ball()
score = Score()

screen.listen()


def move_paddle(key1, key2, function1, function2):
    """Move paddle when key pressed.\n
    This is a high order function => passing function as argument inside another
    function """
    screen.onkey(key=key1, fun=function1)
    screen.onkey(key=key2, fun=function2)


move_paddle(key1="Up", key2="Down", function1=right_paddle.move_upwards, function2=right_paddle.move_downwards)
move_paddle(key1="w", key2="s", function1=left_paddle.move_upwards, function2=left_paddle.move_downwards)

is_game_on = True


def bouncing_ball():
    """control a ball collision with paddle"""
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(
            left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


while is_game_on:
    time.sleep(0.1)  # To see a ball we have to slow down our while loop
    screen.update()
    ball.move()
    bouncing_ball()
    if ball.xcor() > 380:
        ball.reset_ball_position()
        score.update_score(position="right")
    elif ball.xcor() < -380:
        ball.reset_ball_position()
        score.update_score(position="left")
screen.exitonclick()
