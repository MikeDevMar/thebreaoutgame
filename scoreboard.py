from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 180)
        self.write(self.score, align='center', font=('Courier', 40, 'normal'))

    def add_score(self):
        self.score +=1
        self.update_scoreboard()
