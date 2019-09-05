# coding: utf-8

from model.conferenceModel import conferenceModel

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
        # model = speakerModel()
        # data = {}
        # data["firstname"] = input("Prénom : ")
        # data["lastname"] = input("Nom : ")
        # data["job"] = input("Profession : ")
        # data["description"] = input("Présentation : ")
        # speaker = Speaker(data)
        # if model.add_speaker(speaker):
        #     print("Le nouvel intervenant a bien été enregistré")

    def delete_conference(self):
        pass
