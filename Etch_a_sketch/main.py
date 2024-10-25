# Importing  modules
from turtle import Turtle, Screen

# Initializing Turtle and Screen
tim = Turtle()  # Create a turtle object
screen = Screen()  # Create a screen object

# Function to move turtle forward
def move_forward():
    tim.forward(10)

# Function to move turtle backwards
def move_backwards():
    tim.backward(10)

# Function to turn turtle left
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

# Function to turn turtle right
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

# Function to clear drawing and reset turtle position
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Function to change pen color to red
def change_pen_color_red():
    tim.pencolor("red")

# Function to change pen color to green
def change_pen_color_green():
    tim.pencolor("green")

# Function to change pen color to blue
def change_pen_color_blue():
    tim.pencolor("blue")

# Function to increase pen thickness
def increase_pen_thickness():
    tim.pensize(tim.pensize() + 1)

# Function to decrease pen thickness
def decrease_pen_thickness():
    if tim.pensize() > 1:
        tim.pensize(tim.pensize() - 1)

# Listen to key events
screen.listen()

# Key bindings for different functions
screen.onkey(move_forward, "w")  # Move forward on 'w' key
screen.onkey(move_backwards, "s")  # Move backwards on 's' key
screen.onkey(turn_left, "a")  # Turn left on 'a' key
screen.onkey(turn_right, "d")  # Turn right on 'd' key
screen.onkey(clear, "c")  # Clear screen on 'c' key
screen.onkey(change_pen_color_red, "1")  # Change pen color to red on '1' key
screen.onkey(change_pen_color_green, "2")  # Change pen color to green on '2' key
screen.onkey(change_pen_color_blue, "3")  # Change pen color to blue on '3' key
screen.onkey(increase_pen_thickness, "KP_Add")  # Increase pen thickness on '+' key (numeric keypad)
screen.onkey(decrease_pen_thickness, "KP_Subtract")  # Decrease pen thickness on '-' key (numeric keypad)

# Exit the screen on click
screen.exitonclick()