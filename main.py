import time
import turtle as t
import snake
from food import Food

# TODO - control the snake
# TODO - detect collision with food
# TODO - create scoreboard
# TODO - detect collision with wall
# TODO - detect collision with tail

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
player = snake.Snake()
food = Food()

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.turn_left, "Left")
screen.onkey(player.turn_right, "Right")

coord_index = 0

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    player.move()

    #detect collision from wall
    if player.head.distance(food) <  15:
        print("Nom Nom Nom")
        food.refresh()

screen.exitonclick()
