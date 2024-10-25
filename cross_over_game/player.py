from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        """
        Initialize the Player object.

        Attributes:
        - shape: Turtle shape set to "turtle".
        - color: Turtle color set to "black".
        - position: Starts at STARTING_POSITION (-280 on y-axis).
        - heading: Faces upwards (90 degrees).
        """
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        """
        Move the player turtle upwards by MOVE_DISTANCE.
        """
        self.forward(MOVE_DISTANCE)

    def is_player_finish_line(self):
        """
        Check if the player has reached the finish line.

        Returns:
        - True if player's y-coordinate is greater than FINISH_LINE_Y (280),
          indicating the player has reached the finish line.
        - False otherwise.
        """
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        """
        Reset the player's position to the starting position (STARTING_POSITION).
        """
        self.goto(STARTING_POSITION)
