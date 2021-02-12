"""This will handle a score of a player"""
from turtle import Turtle


class Score(Turtle):
    """Show score and keep a record off it"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.goto(0, 270)
        self.color("white")
        self.write(arg=f"Score {self.player1_score} || {self.player2_score}", align="center",
                   font=("Arial", 18, "normal"))

    def update_score(self, position):
        """Increase a score by 1"""
        if position == "right":
            self.player1_score += 1
            self.clear()
            self.write(arg=f"Score {self.player1_score} || {self.player2_score}", align="center",
                       font=("Arial", 18, "normal"))
        elif position == "left":
            self.player2_score += 1
            self.clear()
            self.write(arg=f"Score {self.player1_score} || {self.player2_score}", align="center",
                       font=("Arial", 18, "normal"))
