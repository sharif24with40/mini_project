# Import the logo from my own ceaser_art module
from ceaser_art import logo

# Print the logo
print(logo)

# Define the alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Define the caesar function for both encoding and decoding
def caesar(text, shift, direction):
    result = ""  # Initialize result string
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)  # Find the index of the letter
            if direction == "encode":
                new_position = (position + shift) % 26  # Calculate new position for encoding
            elif direction == "decode":
                new_position = (position - shift) % 26  # Calculate new position for decoding
            new_letter = alphabet[new_position]  # Find the letter at the new position
            result += new_letter  # Append the new letter to the result
        else:
            result += letter  # If the character is not in the alphabet, add it unchanged
    print(f"The {direction}d text is: {result}")  # Print the result

# Run an infinite loop to keep the program running
while True:
    # Prompt user to input the direction (encode/decode/exit)
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt, or 'exit' to quit:\n").lower()
    
    if direction == "exit":
        print("Goodbye")  # Print goodbye message
        break  # Exit the loop and terminate the program

    # Prompt user to input the message to be encoded/decoded
    text = input("Type your message:\n").lower()
    # Prompt user to input the shift number
    shift = int(input("Type the shift number:\n"))

    # Check if the direction is valid
    if direction in ["encode", "decode"]:
        # Call the caesar function with the inputs
        caesar(text, shift, direction)
    else:
        print("Please enter a valid input.")  # Print error message for invalid input
