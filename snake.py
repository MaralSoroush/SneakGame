from os import system
import time
import turtle
import random

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DISTANCE = 20


class Snake:
    def __init__(self):
        turtle.mode("standard")
        self.initial_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_body = []
        self.creat_snake()

    def creat_snake(self):
        for position in self.initial_positions:
            self.add_segment(position)

    def add_segment(self, position):
        self.new_part = turtle.Turtle(shape="square")
        self.new_part.penup()
        self.new_part.color("white")
        self.new_part.goto(position)
        self.snake_body.append(self.new_part)

    def reset(self):
        for part in self.snake_body:
            part.goto(10000, 10000)
        self.snake_body.clear()
        self.creat_snake()

    def move_snake(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i-1].xcor()
            new_y = self.snake_body[i-1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.snake_body[0].forward(DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def new_segment(self):
        self.add_segment(self.snake_body[-1].position())
