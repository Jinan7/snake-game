from turtle import Turtle, color
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.y = None
        self.x = None
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=1)
        self.set_position()


    def set_position(self):
        self.x = random.randint(-200, 200)
        self.y = random.randint(-200, 200)
        self.goto(self.x, self.y)

    def get_size(self):
        return 20*0.5 