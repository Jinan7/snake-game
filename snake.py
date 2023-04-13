from turtle import Turtle
from cell import *
class Snake:
    def __init__(self, no_of_cells):
        self.no_of_cells = no_of_cells
        self.snake = []

    def createSnake(self):
        for pos in range(0, self.no_of_cells):
           cell = Cell(10*pos,0,0)
           self.snake.append(cell);