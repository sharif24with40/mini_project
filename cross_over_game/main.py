from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic screen updates

# Create instances of Player, CarManager, and Scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for key events
screen.listen()
screen.onkey(player.move, "Up")  # Player moves when the "Up" key is pressed

game_is_on = True

while game_is_on:
    time.sleep(0.1)  # Control the game speed
    screen.update()  # Update the screen manually

    # Create a new car and move all cars
    car_manager.create_car()
    car_manager.move_cars()

    # Check for collision with player and cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check if player reaches the finish line
    if player.is_player_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

# Exit the game when the screen is clicked
screen.exitonclick()
