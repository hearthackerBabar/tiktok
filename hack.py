import os
import time
import random

# Red color text
def print_red(text):
    print(f"\033[91m{text}\033[0m")

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Welcome message (larger text and centered)
print("\033[1;32;40m")
print("\n\n")
print("     WELCOME TO THE TIKTOK INFO TOOL".center(80))  # Bada welcome text in green
print("\n")
time.sleep(0.5)

# Hacker-style "TikTok Info Tool" message
print("\033[1;33;40m")
print("Initializing TikTok Info Tool...".center(80))
time.sleep(1)

# Hacker-style theme with logo and animation
print("\n")
time.sleep(0.5)

# Display hacker logo (simulated)
print("\033[1;32;40m")
print("""
████████╗██╗████████╗███████╗████████╗██╗  ██╗███████╗
╚══██╔══╝██║╚══██╔══╝██╔════╝╚══██╔══╝██║  ██║██╔════╝
   ██║   ██║   ██║   █████╗     ██║   ███████║█████╗  
   ██║   ██║   ██║   ██╔══╝     ██║   ██╔══██║██╔══╝  
   ██║   ██║   ██║   ███████╗   ██║   ██║  ██║███████╗
   ╚═╝   ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
""".center(80))
time.sleep(1)

# Ask for username
username = input("Enter Username: ")

# Display the entered username
print(f"Hello, {username}!")

# Show loading for 20 seconds with hacker-like animation
print("Initializing", end="")
for i in range(5):  # Total time 20 seconds with 4 dots in between
    time.sleep(4)  # 4 seconds for each part of the loading
    print(".", end="", flush=True)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[92mHacking...\033[0m")
    print(f"Entering Data for {username}...")  # Simulate hacker environment

time.sleep(1)  # Final pause to simulate end of loading
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
