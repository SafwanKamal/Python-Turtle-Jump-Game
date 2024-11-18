from turtle import Screen, Turtle, mainloop
from random import choice, randint
from math import ceil

scr = Screen()
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
HEIGHT_PADDING = 50
WIDTH_PADDING = 30
TURTLE_HEIGHT_PADDING = 20
ACCEPTABLE_DISTANCE = 17
INTERVEL_MS_DIVIDER_STEP = 0.4


COLORS = ['red', 'blue', 'yellow', 'purple', 'green', 'orange', 'pink', 'magenta']
INTERVAL_MS = 120
FONT=("Courier", 24, "normal")

scr.bgcolor('gray')
scr.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# scr.mode('world')
# scr.setworldcoordinates(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

scr.tracer(0)
scr.title("TURTLE JUMP")

cars = []
game_over = False
current_level = 1
intervel_ms_divider = 2


### IMPLEMENTING CAR CLASS ###
class Car(Turtle):
    def __init__(self, spd):
        super().__init__()
        self.color(choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_wid=1.1, stretch_len=2, outline=None)
        self.penup()
        self.positioner()
        self.speed(spd)
        self.edge_checker()
        self.move()

        
    def positioner(self, first_time = True):
        self.hideturtle()
        self.speed(0)
        self.y_cor = randint(-WINDOW_HEIGHT // 2 + HEIGHT_PADDING, WINDOW_HEIGHT // 2)
        if first_time:
            self.x_cor = randint(-WINDOW_WIDTH // 2, WINDOW_WIDTH // 2)
        else:
            self.x_cor = + WINDOW_WIDTH // 2
        self.goto(self.x_cor, self.y_cor)
        self.showturtle()

    def move(self):
        current_position = self.pos()
        self.forward(-10)
        #self.goto(current_position[0] - 10, current_position[1])
        scr.ontimer(self.move, INTERVAL_MS)

    def edge_checker(self):
        current_position = self.pos()
        if current_position[0] < -WINDOW_WIDTH // 2:
            self.positioner(first_time=False)
        scr.ontimer(self.edge_checker, INTERVAL_MS)

    # def collision_checker(self, plyr):
    #     pass



### IMPLEMENTING CAR GENERATOR CLASS ###
### This class also handles collision with the player ###


class Car_generator(Car):
    global cars, game_over, scr, plyr

    def __init__(self, car_number) -> None:
        self.car_number = car_number
        self.generate_cars()
        self.collision_checker()

    def generate_cars(self):
        for _ in range(self.car_number):
            c = Car(5)
            cars.append(c)
        # print(cars)
    def collision_checker(self):
        global cars, game_over, scr, plyr

        for car in cars:
            dis = plyr.distance(car)
            #print(dis)
            if dis < ACCEPTABLE_DISTANCE:
                game_over = True
                #scr.bye()

        scr.ontimer(self.collision_checker, INTERVAL_MS)

    def update_car_speed(self):
        pass

#### IMPLEMENTING TURTLE PLAYER CLASS ##
### This class also checks for winning conditions in the level ###
    
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape('turtle')
        self.color('white')
        self.speed(0)
        self.goto(0, - WINDOW_HEIGHT // 2 + TURTLE_HEIGHT_PADDING)
        self.left(90)
        self.showturtle()
        self.can_move = True
        self.can_move_updater()
        self.level_win_checker()

    def can_move_updater(self):
        self.can_move = True
        scr.ontimer(self.can_move_updater, INTERVAL_MS // 4)

    def move(self):
        if self.can_move:
            self.forward(10)
            self.can_move = False

    def positioner(self):
        self.hideturtle()
        self.speed(0)
        self.goto(0, - WINDOW_HEIGHT // 2 + TURTLE_HEIGHT_PADDING)
        self.showturtle()

    def level_win_checker(self):
        global car_generator, INTERVAL_MS, current_level, intervel_ms_divider
        current_position = self.pos()
        if current_position[1] > WINDOW_HEIGHT // 2:
            self.positioner()
            current_level += 1
            level_board()
            INTERVAL_MS = int(ceil(INTERVAL_MS / intervel_ms_divider))
            intervel_ms_divider -= INTERVEL_MS_DIVIDER_STEP

            if intervel_ms_divider < 1:
                intervel_ms_divider = 1.1
        scr.ontimer(self.level_win_checker, INTERVAL_MS)


### IMPLEMENTING GLOBAL GAME FUNCTIONS ###
### These are implemented here as they are not that easily classified under a class ###


def stop_window():
    global intervel_ms
    scr.tracer(0)

    scr.ontimer(stop_window, INTERVAL_MS // 4)

def update_window():
    global intervel_ms
    if not game_over:
        scr.update()

    scr.ontimer(update_window, INTERVAL_MS // 4)

def game_over_check():
    global scr, game_over
    if game_over:
        game_over_turtle = Turtle(visible=False)
        game_over_turtle.forward(WINDOW_WIDTH / 60)
        game_over_turtle.write("GAME OVER", font=FONT, align='Center')
        game_over_turtle.right(90)
        game_over_turtle.forward(WINDOW_HEIGHT / 30)
        game_over_turtle.write("Click On The Screen To Exit", font=FONT, align='Center')

        #scr.bye()

    scr.ontimer(game_over_check, INTERVAL_MS)

def level_board():
    global scr, current_level, level_board_turtle
    level_board_turtle.clear()
    level_board_turtle.penup()
    level_board_turtle.speed(0)
    level_board_turtle.goto(- WINDOW_WIDTH // 2 + WIDTH_PADDING, WINDOW_HEIGHT // 2 - HEIGHT_PADDING)
    level_board_turtle.pendown()
    level_board_turtle.write(f"LEVEL : {current_level}", font=FONT)



#scr.tracer(20)



plyr = Player()

scr.listen()
scr.onkey(fun=plyr.move, key='space')

stop_window()
car_generator = Car_generator(15)
game_over_check()

level_board_turtle = Turtle(visible=False)
level_board()

update_window()
scr.exitonclick()

scr.mainloop()