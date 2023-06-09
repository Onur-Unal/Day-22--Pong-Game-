from turtle import Turtle

COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.l_Score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 230)
        self.write(self.l_Score, align=ALIGNMENT, font=FONT)
        self.goto(50, 230)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_Score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()






