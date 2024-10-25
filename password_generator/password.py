import random
import string

print("Welcome to the PyPassword Generator!")

while True:
    try:
        num_letter = int(input("How many letters would you like in your password? "))
        num_symbols = int(input("How many symbols would you like in your password? "))
        
        if num_letter <= 0 and num_symbols <= 0:
            print("Please enter a positive value.")
            continue
        
        letters = string.ascii_letters  # includes both lowercase and uppercase letters
        symbols = "!@#$%^&*()_+-=[]{};:,.<>?/"  # expanded list of symbols
        
        password = ""
        
        for i in range(num_letter):
            password += random.choice(letters)
        for j in range(num_symbols):
            password += random.choice(symbols)
        
        password_list = list(password)
        random.shuffle(password_list)
        
        generated_password = "".join(password_list)
        
        print(f"Generated Password: {generated_password}")
        
        generate_again = input("Do you want to generate again? Type 'Yes' or 'No': ")
        
        if generate_again.lower() != "yes":
            break
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")
