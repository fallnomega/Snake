import turtle as t

#TODO - create a snake body
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
snake = []
for x in range(3):
    x = t.Turtle()
    x.color("white")
    x.shape("square")
    x.setx(x_pos)
    snake.append(x)
    x_pos-=20


screen.exitonclick()
