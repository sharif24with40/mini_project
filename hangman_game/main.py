import random
from hangman_art import stages  # Importing hangman stages for visual representation of lives
from hangman_words import word_list  # Importing a list of words to choose 
from hangman_art import logo  # Importing the logo to display at the start of the game

# Randomly choose a word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize the game state variables
end_of_game = False
lives = 6

# Display the game logo
print(logo)

# Create a list to represent the blanks in the chosen word
display = []
for _ in range(word_length):
    display += "_"

# Main game loop
while not end_of_game:
    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")

    # Update the display list with the guessed letter if it is in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If the guessed letter is not in the chosen word, reduce the lives count
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was: {chosen_word}")  # Reveal the word when the game is lost

    # Print the current state of the display (with blanks and correctly guessed letters)
    print(f"{' '.join(display)}")

    # Check if the player has guessed all letters and won the game
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Display the current hangman stage corresponding to the number of lives left
    print(stages[lives])
