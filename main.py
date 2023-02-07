import time
import turtle as t


# TODO - control the snake
# TODO - detect collision with food
# TODO - create scoreboard
# TODO - detect collision with wall
# TODO - detect collision with tail


def move_foward():
    for segment in snake:
        segment.forward(20)


def turn_right():
    for segment in snake:
        segment.setheading(270)


def turn_left():
    for segment in snake:
        segment.setheading(90)


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# make snake
def make_snake(i, pos):
    i.penup()
    i.color("white")
    i.shape("square")
    i.goto(pos)


game_is_on = True
snake = []
start_coord = [(0, 0), (-20, 0), (-40, 0)]
coord_index = 0
for x in range(3):
    x = t.Turtle()
    make_snake(x, start_coord[coord_index])
    coord_index += 1
    snake.append(x)

while game_is_on:
    screen.update()
    time.sleep(.1)
    for seg_num in range(len(snake) - 1, 0, -1):
        new_x = snake[seg_num - 1].xcor()
        new_y = snake[seg_num - 1].ycor()
        snake[seg_num].goto(new_x, new_y)
    snake[0].forward(20)

screen.exitonclick()
