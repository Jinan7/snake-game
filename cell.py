from turtle import Turtle

class Cell:
    def __init__(self, x, y, color):
        self.height = 20
        self.width = 20
        self.color=color
        self.x=x
        self.y=y
        self.cell = Turtle("square")