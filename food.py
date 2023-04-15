from turtle import Turtle, color
from random import Random

class Food(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=1)
        self.set_position(x,y)


    def set_position(self,x,y):
        self.x = x
        self.y = y
        self.goto(x, y)