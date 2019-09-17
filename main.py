# coding: utf-8
import os
import time

from view.speakerView import speakerView
from view.conferenceView import conferenceView

# Main file acting like a routing system
# Call the right method from the view, depending on user input

def speaker_actions():
    """Show the different actions relate to speakear entity"""
    # instanciate the view with the methods holding the code logic
    view = speakerView()
    action = ""
    while action != "r":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Gestion de la base intervants")
        print("Que souhaitez vous faire ? (l: liste, n: nouveau, s: suppression, r: retour)")
        action = input(": ")
        # call the right method from the view according to user input
        if action == "l":
            view.show_speakers()
        elif action == "n":
            view.new_speaker()
        elif action == "s":
            view.delete_speaker()
        time.sleep(3)

def conference_actions():
    """Show the different actions relate to conference entity"""
    # instanciate the view with the methods holding the code logic
    view = conferenceView()
    action = ""
    while action != "r":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Gestion des interventions au programme")
        print("Que souhaitez vous faire ? (l: liste, n: nouvelle, s: suppression, r: retour)")
        action = input(": ")
        # call the right method from the view according to user input
        if action == "l":
            view.show_conferences()
        elif action == "n":
            view.new_conference()
        elif action == "s":
            view.delete_conference()
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
    # call the right action function according to user input
    if action == "c":
        conference_actions()
    elif action == "i":
        speaker_actions()

# Leave the program
print("A bientôt sur Plan&Go")
time.sleep(3)
exit()
