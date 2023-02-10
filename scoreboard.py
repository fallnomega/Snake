from turtle import Turtle


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(0, 280)
        self.score = 0
        self.highscore = self.open_score_file()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.highscore}", font=('Arial', 16, 'normal'))

    def add_to_score(self):
        self.score += 1
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        # self.update_board()
        self.write(f"GAME OVER\nScore: {self.score} High Score: {self.highscore}", align="center",
                   font=('Arial', 32, 'normal'))

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.score = 0
            self.update_board()
        else:
            self.score = 0
            self.update_board()

    def update_board(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score_file.txt", 'w') as file:
                x = str(self.highscore)
                file.write(x)
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore} ", font=('Arial', 16, 'normal'))

    def open_score_file(self):
        file = open("high_score_file.txt", 'r')
        contents = file.read()
        print(contents)
        file.close()
        x = int(contents)
        return x
