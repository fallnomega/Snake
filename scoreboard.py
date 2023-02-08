from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(0,280)
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score} ",font=('Arial', 16, 'normal'))

    def add_to_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score} ", font=('Arial', 16, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center", font=('Arial', 32, 'normal'))
