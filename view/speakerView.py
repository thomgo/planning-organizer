# coding: utf-8

from model.speakerModel import speakerModel
from model.entities.speaker import Speaker

class speakerView():
    """View or controller taking care of all the logic related to speaker in the app."""

    def __init__(self):
        pass

    def show_speakers(self):
        model = speakerModel()
        speakers = model.get_speakers()
        if speakers:
            for speaker in speakers:
                print(speaker)
        else:
            print("pas d'intervenants")
        input("Appuyez sur une touche pour continuer")

    def new_speaker(self):
        model = speakerModel()
        data = {}
        data["firstname"] = input("Prénom : ")
        data["lastname"] = input("Nom : ")
        data["job"] = input("Profession : ")
        data["description"] = input("Présentation : ")
        speaker = Speaker(data)
        if model.add_speaker(speaker):
            print("Le nouvel intervenant a bien été enregistré")

    def delete_speaker(self):
        model = speakerModel()
        id = input("L'id de l'intervenant à supprimer : ")
        if model.delete_speaker(id):
            print("L'intervenant a bien été supprimé")
