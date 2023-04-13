from turtle import Turtle

class Cell:
    def __init__(self, height, width, color, x, y):
        self.height=height
        self.width=width
        self.color=color
        self.x=x
        self.y=y
        self.cell = Turtle("square")