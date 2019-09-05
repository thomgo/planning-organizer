# coding: utf-8
import os
import time

from view.speakerView import speakerView
from view.conferenceView import conferenceView

# Main file acting like a routing system
# Call the right method from the view, depending on user input

def speaker_actions():
    view = speakerView()
    action = ""
    while action != "r":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Gestion de la base intervants")
        print("Que souhaitez vous faire ? (l: liste, n: nouveau, s: suppression, r: retour)")
        action = input(": ")
        if action == "l":
            view.show_speakers()
        elif action == "n":
            view.new_speaker()
        elif action == "s":
            pass
        time.sleep(3)

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
    print("Que souhaitez vous gérez ? (c: conférences, i: intervenants, q: quitter)")
    action = input(": ")
    if action == "c":
        pass
    elif action == "i":
        speaker_actions()

# Leave the program
print("A bientôt sur Plan&Go")
time.sleep(3)
exit()
