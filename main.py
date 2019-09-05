# coding: utf-8
import os
import time
from view.speakerView import speakerView

# Main file acting like a routing system
# Call the right method from the view, depending on user input

# Simple intro for the app
os.system('cls' if os.name == 'nt' else 'clear')
print("Plan&Go vous organisez, nous planifions")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Le logiciel numéro 1 de la planification de conférence")
time.sleep(3)

# The action the user wants to do, by default nothing
action = ""

# while the user does not chose to leave the program
while action != 'q':
    os.system('cls' if os.name == 'nt' else 'clear')
    action = input(": ")

# Leave the program
print("A bientôt sur Plan&Go")
time.sleep(3)
exit()
