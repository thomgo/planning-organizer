# coding: utf-8

from model.speakerModel import speakerModel
from model.entities.speaker import Speaker

class speakerView():
    """View or controller taking care of all the logic related to speaker in the app."""
    model = speakerModel()

    def __init__(self):
        pass

    def show_speakers(self):
        """Display all the speakers from database to the screen"""
        # retrieve speakers from database
        speakers = speakerView.model.get_speakers()
        # if we have speakers we show them in a loop
        if speakers:
            for speaker in speakers:
                print(speaker)
        # otherwise we print a message
        else:
            print("pas d'intervenants")
        input("Appuyez sur une touche pour continuer")

    def new_speaker(self):
        """Displays inputs to register a new speaker in the database"""
        # start an empty dictionnary to hold speaker's information
        data = {}
        data["firstname"] = input("Prénom : ")
        data["lastname"] = input("Nom : ")
        data["job"] = input("Profession : ")
        data["description"] = input("Présentation : ")
        # instanciate a speaker with the info
        speaker = Speaker(data)
        # if the registering is succesfull print a success message
        if speakerView.model.add_speaker(speaker):
            print("Le nouvel intervenant a bien été enregistré")

    def delete_speaker(self):
        """Display an input to delete a speaker from database by his ID"""
        id = input("L'id de l'intervenant à supprimer : ")
        # if the delete is succesfull print a success message
        if speakerView.model.delete_speaker(id):
            print("L'intervenant a bien été supprimé")
