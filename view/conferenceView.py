# coding: utf-8

from model.conferenceModel import conferenceModel

class conferenceView():
    """View or controller taking care of all the logic related to conference in the app."""

    def __init__(self):
        pass

    def home(self):
        model = conferenceModel()
        conferences = model.get_conferences()
        if conferences:
            print("Voici les conférence")
        else:
            print("Nous n'avons aucune conférence de prévue pour l'instant")
