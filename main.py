import time
import turtle as t
import snake
from food import Food
from scoreboard import scoreboard

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
scoreboard = scoreboard()

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

    #detect collision from food
    if player.head.distance(food) <  15:
        scoreboard.add_to_score()
        food.refresh()
        player.extend()

    #detect wall collision
    if player.head.xcor() > 280 or player.head.xcor() < -280 or player.head.ycor() > 280 or player.head.ycor() < -280 :
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tail
    #if player.head collides with any segment of the tail, trigger GAMEOVER

    for segment in player.segments:
        if segment == player.head:
            pass
        elif player.head.distance(segment) < 10:
            scoreboard.game_over()



screen.exitonclick()
