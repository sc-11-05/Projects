from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 350)
        self.write(self.left_score, align= ALIGNMENT, font= FONT)
        self.goto(100, 350)
        self.write(self.right_score, align= ALIGNMENT, font= FONT)
    
    def left_point(self):
        self.left_score += 1
        self.update_score()
    
    def right_point(self):
        self.right_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)

        if (self.left_score > self.right_score):
            self.write("Player 1 Wins", align= ALIGNMENT, font= FONT)
        
        elif (self.left_score < self.right_score):
            self.write("Player 2 Wins", align= ALIGNMENT, font= FONT)
        
        else:
            self.write("Draw", align= ALIGNMENT, font= FONT)
            
