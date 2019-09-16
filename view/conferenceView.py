# coding: utf-8

from model.conferenceModel import conferenceModel
from model.entities.conference import Conference

class conferenceView():
    """View or controller taking care of all the logic related to conference in the app."""

    def __init__(self):
        pass

    def show_conferences(self):
        model = conferenceModel()
        conferences = model.get_conferences()
        if conferences:
            print("Voici les conférence")
        else:
            print("Nous n'avons aucune conférence de prévue pour l'instant")

    def new_conference(self):
        pass
        model = conferenceModel()
        data = {}
        data["title"] = input("Titre : ")
        data["summary"] = input("Résumé : ")
        data["event_date"] = input("Date (jj/mm/aaaa): ")
        data["event_time"] = input("Heure (hh:mm): ")
        data["speaker"] = input("Intervenant : ")
        conference = Conference(data)
        print(conference)
        if model.add_conference(conference):
            print("la conférence a bien été enregistrée")

    def delete_conference(self):
        pass
