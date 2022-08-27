from os import system
import turtle
import random
import time
import snake
import food
import score

# screen initializing
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# turning off the animation
screen.tracer(0)
# make a snake object
new_snake = snake.Snake()
new_food = food.Food()
# make sreen listen for input keys
screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")
# score
new_score = score.Score()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.06)
    new_snake.move_snake()

    # detect collision with food
    if new_snake.snake_body[0].distance(new_food) < 15:
        new_food.make_new_food()
        new_snake.new_segment()
        new_score.score_update()

    # detect collision with wall
    contition_1 = new_snake.snake_body[0].xcor(
    ) > 290 or new_snake.snake_body[0].xcor() < -290
    condition_2 = new_snake.snake_body[0].ycor(
    ) > 290 or new_snake.snake_body[0].ycor() < -290
    if contition_1 or condition_2:
        new_snake.reset()
        new_score.reset_score()

    # detect collision with tail
    for i in new_snake.snake_body[1:]:
        if new_snake.snake_body[0].distance(i) < 10:
            new_snake.reset()
            new_score.reset_score()


screen.exitonclick()
