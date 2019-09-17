# coding: utf-8

from model.conferenceModel import conferenceModel
from model.entities.conference import Conference

class conferenceView():
    """View or controller taking care of all the logic related to conference in the app."""
    model = conferenceModel()

    def __init__(self):
        pass

    def show_conferences(self):
        """Display all the conferences from database to the screen"""
        # retrieve conferences from the database
        conferences = conferenceView.model.get_conferences()
        # if we have conferences we show them in a loop
        if conferences:
            for conference in conferences:
                print(conference)
        # otherwise we print a message
        else:
            print("Nous n'avons aucune conférence de prévue pour l'instant")
        input("Appuyez sur une touche pour continuer")

    def new_conference(self):
        """Displays inputs to register a new conference in the database"""
        # start an empty dictionnary to hold conference's information
        data = {}
        data["title"] = input("Titre : ")
        data["summary"] = input("Résumé : ")
        data["event_date"] = input("Date (jj/mm/aaaa): ")
        data["event_time"] = input("Heure (hh:mm): ")
        data["speaker"] = input("Id de l'intervenant : ")
        # instanciate a conferance with the info
        conference = Conference(data)
        # if the registering is succesfull print a success message
        if conferenceView.model.add_conference(conference):
            print("la conférence a bien été enregistrée")

    def delete_conference(self):
        """Display an input to delete a conference from database by his ID"""
        id = input("L'id de la conférence à annuler : ")
        # if the delete is succesfull print a success message
        if conferenceView.model.delete_conference(id):
            print("La conférence a bien été supprimée")
