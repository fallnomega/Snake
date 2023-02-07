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

x_pos = 0
snake = t.Turtle()
snake.shapesize(1,-3,1)
snake.color("white")
snake.shape("square")
snake.setx(x_pos)
x_pos-=20


screen.exitonclick()
