import pandas as pd

# Read the CSV file containing the NATO phonetic alphabet
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Get a word from the user and convert it to uppercase
words = input("Enter a word: ").upper()

# Create a dictionary from the data where the letter is the key and the code is the value
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of phonetic codes corresponding to each letter in the input word
result = [phonetic_dict[letter] for letter in words]

# Print the resulting list of phonetic codes
print(result)
