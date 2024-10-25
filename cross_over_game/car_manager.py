from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "violet", "purple", "pink", "brown"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        """
        Initialize a CarManager object.

        Attributes:
        - all_cars: A list to store all car Turtle objects.
        - car_speed: Initial speed of cars, starts at STARTING_MOVE_DISTANCE.
        """
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        Create a new car Turtle object with a random chance.

        Randomly decides if a new car should be created based on a random number generator.
        """
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """
        Move all cars in the `all_cars` list towards the left.

        Uses the current `car_speed` attribute to determine how far each car moves per frame.
        """
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """
        Increase the speed of the cars for the next level.

        This method increments the `car_speed` attribute by `MOVE_INCREMENT` units,
        effectively making the cars move faster as the game progresses.
        """
        self.car_speed += MOVE_INCREMENT

