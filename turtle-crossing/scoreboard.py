from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", font=("Courier", 16, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", font=("Courier", 16, "normal"))
    
    def level_up(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "bold"))

