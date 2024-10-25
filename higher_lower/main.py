from hg_art import logo, logo1  # Importing logos from hg_art my own module
from game_data import data      # Importing game data from game_data my own  module
import os
import random

# Function to randomly select an account from the data
def random_account():
    return random.choice(data)

# Function to format account data into a readable string
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Function to check if the guessed account has more followers
def check_answer(guess, a_followers, b_followers):
    return a_followers > b_followers if guess == "a" else b_followers > a_followers

# Main game function
def game():
    print(logo)  # Print the game logo
    score = 0  # Initialize the score counter
    game_should_continue = True  # Flag to control game loop

    # Initialize accounts A and B with random accounts
    account_a = random_account()
    account_b = random_account()

    while game_should_continue:
        account_a = account_b  # Move account B to account A
        account_b = random_account()  # Select a new random account for account B

        while account_a == account_b:
            account_b = random_account()  # Ensure account A and account B are different

        # Display the comparison between account A and account B
        print(f"Compare A: {format_data(account_a)}")
        print(logo1)  # Print logo1 (assuming it's a different logo)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()  # User input for guess
        a_follower_count = account_a["follower_count"]  # Follower count of account A
        b_follower_count = account_b["follower_count"]  # Follower count of account B

        # Check if the guess is correct
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        os.system("clear")  # Clear the screen for better user interface (Linux/Mac)

        print(logo)  # Reprint the logo after clearing the screen

        if is_correct:
            score += 1  # Increase score if guess is correct
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False  # End game if guess is incorrect
            print(f"Sorry, that's wrong. Final score: {score}")

# Run the game
game()
