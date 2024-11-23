import os

# Red color text
def print_red(text):
    print(f"\033[91m{text}\033[0m")

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Welcome message
print_red("Welcome!")

# Ask for username
username = input("Enter Username: ")

# Display the entered username
print(f"Hello, {username}!")
