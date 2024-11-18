from turtle import Turtle
from random import choice, randint

colors = ['red', 'blue', 'yellow', 'purple', 'green', 'orange']

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

class Car(Turtle):
    def __init__(self, spd):
        super().__init__()
        self.color(choice(colors))
        self.shape('Square')
        self.shapesize(stretch_wid=2, stretch_len=1, outline=None)
        self.positioner()
        self.speed(spd)
        
    def positioner(self): 
        self.hideturtle()
        self.speed(0)
        self.x_cor = randint(-WINDOW_HEIGHT // 2, WINDOW_HEIGHT // 2)
        self.y_cor = randint(-WINDOW_WIDTH // 2, WINDOW_WIDTH // 2)
        self.goto(self.x_cor, self.y_cor)
        self.showturtle()

    