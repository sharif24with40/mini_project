import random
from number_art import logo  # logo is imported correctly from my own number_art module

# Display the game logo and welcome message
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    # Prompt user to choose difficulty level and handle input validation
    while True:
        mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if mode == "easy":
            chances = 10  # Set chances to 10 for easy mode
            break
        elif mode == "hard":
            print("You have 5 attempts remaining to guess the number.")
            chances = 5  # Set chances to 5 for hard mode
            break
        else:
            print("Invalid input. Please choose 'easy' or 'hard'.")
            continue
    
    # Generate a random number between 1 and 100
    computer_guess = random.randint(1, 100)
    
    # Loop for the number of chances available
    for i in range(1, chances + 1):
        print(f"You have {chances - i + 1} attempt(s) remaining to guess the number.")
        
        # Handle user input for guessing the number with error handling
        while True:
            try:
                guess = int(input("Make a guess: "))
                break  # Exit the loop if input is a valid integer
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        # Compare user's guess with the computer's number
        if guess == computer_guess:
            print(f"Correct! You win in {i} attempt(s).")
            break  # Exit the loop if guess is correct
        elif guess > computer_guess:
            print("Too high.")
        else:
            print("Too low.")
    
    else:
        # If all chances are exhausted without correct guess
        print(f"Sorry, you ran out of attempts. The correct number was {computer_guess}.")
    
    # Prompt user to play again or quit, with input validation
    while True:
        play_again = input("Do you want to play again? Type 'yes' or 'no': ").strip().lower()
        if play_again == "yes":
            break  # Continue the outer loop to play again
        elif play_again == "no":
            print("Thanks for playing!")
            quit()  # Exit the program if user chooses not to play again
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
