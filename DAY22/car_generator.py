from turtle import Turtle, Screen
from Car import Car
import turtle


scr = turtle.Screen()

scr = Screen()
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

scr.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# scr.mode('world')
# scr.setworldcoordinates(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

class Car_generator(Car):
    def __init__(self, car_number) -> None:
        self.car_number = car_number

    def generate_cars(self):
        for _ in range(self.car_number):
            c = Car(5)
            cars.append(c)

Car_generator(20)
scr.exitonclick()