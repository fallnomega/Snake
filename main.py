import turtle as t


#TODO - move the snake
#TODO - control the snake
#TODO - detect collision with food
#TODO - create scoreboard
#TODO - detect collision with wall
#TODO - detect collision with tail





screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

#make snake
def make_snake():
    x_pos = -30
    snake.shapesize(1,-3,1)
    snake.color("white")
    snake.shape("square")
    snake.goto(-30,0)

game_is_on = True
snake = t.Turtle()
snake.penup()

make_snake()
while game_is_on:
    snake.forward(20)

screen.exitonclick()
