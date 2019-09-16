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
            for conference in conferences:
                print(conference)
        else:
            print("Nous n'avons aucune conférence de prévue pour l'instant")
        input("Appuyez sur une touche pour continuer")

    def new_conference(self):
        model = conferenceModel()
        data = {}
        data["title"] = input("Titre : ")
        data["summary"] = input("Résumé : ")
        data["event_date"] = input("Date (jj/mm/aaaa): ")
        data["event_time"] = input("Heure (hh:mm): ")
        data["speaker"] = input("Id de l'intervenant : ")
        conference = Conference(data)
        if model.add_conference(conference):
            print("la conférence a bien été enregistrée")

    def delete_conference(self):
        model = conferenceModel()
        id = input("L'id de la conférence à annuler : ")
        if model.delete_conference(id):
            print("La conférence a bien été supprimée")
