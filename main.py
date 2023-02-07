import turtle as t


#TODO - move the snake
#TODO - control the snake
#TODO - detect collision with food
#TODO - create scoreboard
#TODO - detect collision with wall
#TODO - detect collision with tail


def move_foward():
    for x in snake:
        x.forward(20)
def turn_right():
    for x in snake:
        x.setheading(270)
def turn_left():
    for x in snake:
        x.setheading(90)


screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

#make snake
def make_snake(i,x_pos):
    # snake.shapesize(1,-3,1)
    x.penup()
    i.color("white")
    i.shape("square")
    i.goto(x_pos,0)

game_is_on = True
snake = []
x_position = 0
for x in range(3):
    x = t.Turtle()
    make_snake(x,x_position)
    snake.append(x)
    x_position-=20

screen.onkeypress(move_foward, 'w')
screen.onkeypress(turn_left, 'a')
screen.onkeypress(turn_right, 'd')

screen.listen()

# while game_is_on:
# #     # snake.forward(20)
#     screen.onkeypress(move_foward, 'w')
#     screen.listen()


screen.exitonclick()
