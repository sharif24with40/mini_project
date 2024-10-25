from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        """
        Initialize the Scoreboard object.

        Attributes:
        - level: Starts at level 1.
        """
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_scoreboard(self):
        """
        Update the scoreboard display with the current level.
        """
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """
        Increase the level by 1 and update the scoreboard.
        """
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Display "GAME OVER" at the center of the screen.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
