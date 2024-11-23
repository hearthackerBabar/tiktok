import os
import time
import random

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

# Show loading for 5 seconds
print("Loading", end="")
for _ in range(3):
    time.sleep(1)
    print(".", end="", flush=True)

time.sleep(1)  # Adding a final pause to simulate the end of loading
print("\n")  # For better formatting

# Displaying random information after loading
print(f"Username: {username}")
print(f"Email: Null")
print(f"Phone Number: +18734777355")
print(f"Country: Canada CA")
print(f"Address: Null")
print(f"Age: Null")
print(f"Occupation: Null")
print(f"Membership Status: Null")
