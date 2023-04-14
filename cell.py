from turtle import Turtle

class Cell:
    def __init__(self, x, y, color):
        self.height = 20
        self.width = 20
        self.color=color
        self.x=x
        self.y=y
        self.cell = Turtle("square")
        self.cell.penup()
        self.set_position(self.x,self.y)

    def set_position(self, x,y):
        self.cell.goto(self.x, self.y)