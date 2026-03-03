from turtle import Turtle

STARTING_POSTIONS = [(-380, 20), (-380,0),(-380, -20)]
MOVE_DISTANCE = 40

class Paddle1:

    def __init__(self):
        self.segments = []
        self.create_paddle()

    
    def create_paddle(self):
        for position in STARTING_POSTIONS:
            self.add_segment(position)
        
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def up(self):
        if self.segments[0].ycor() < 360: 
            for segment in self.segments:
                segment.sety(segment.ycor() + MOVE_DISTANCE)
    
    def down(self):
        if self.segments[-1 ].ycor() > -360:
            for segment in self.segments:
                segment.sety(segment.ycor() - MOVE_DISTANCE)
    
    
