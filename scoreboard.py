from turtle import Turtle


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(0, 280)
        self.score = 0
        self.highscore = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score} ", font=('Arial', 16, 'normal'))

    def add_to_score(self):
        self.score += 1
        self.update_board()


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=('Arial', 32, 'normal'))

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.score = 0
            self.clear()
    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score} ", font=('Arial', 16, 'normal'))


