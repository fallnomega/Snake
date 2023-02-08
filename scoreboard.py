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
        self.score+=10
        self.clear()
        self.write(f"Score: {self.score} ", font=('Arial', 16, 'normal'))