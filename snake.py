from turtle import Turtle
from cell import *
from food import *
class Snake:
    def __init__(self, no_of_cells):
        self.no_of_cells = no_of_cells
        self.snake = []
        self.createSnake()

    def createSnake(self):
        for pos in range(0, self.no_of_cells):
            cell = Cell(-20 * pos, 0, 0)
            self.snake.append(cell)
    def move(self, x, y):
        for pos in range(self.no_of_cells-1, 0, -1):
            self.snake[pos].x = self.snake[pos - 1].x
            self.snake[pos].y = self.snake[pos - 1].y
            self.snake[pos].set_position(self.snake[pos].x, self.snake[pos].y)
        self.snake[0].x += x
        self.snake[0].y += y
        self.snake[0].set_position(self.snake[0].x, self.snake[0].y)

    def has_eaten(self, food):
        return self.snake[0].cell.distance(food.xcor(), food.ycor()) < food.get_size()

    def has_hit_wall(self):
        return (self.snake[0].x >270 or
                self.snake[0].y > 270 or
                self.snake[0].x < -270 or
                self.snake[0].y < -270)