from os import system
import turtle
import random


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("DarkOliveGreen")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.make_new_food()

    def make_new_food(self):
        self.clear()
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
