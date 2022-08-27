from statistics import mode
import string
from telnetlib import DONT
import turtle
ALIGNMETN = "center"
FONT = ("Comic Sans MS", 19, "normal")


class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}",
                   move=True, align=ALIGNMETN, font=FONT)

    def reset_score(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.write_score()

    def score_update(self):
        self.score += 1
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over!",
    #                move=True, align=ALIGNMETN, font=FONT)
