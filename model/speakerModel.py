# coding: utf-8
from .connection import connection
from .entities.speaker import Speaker

class speakerModel():
    """Class to perform all queries related to the speaker table in the database"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        self.db = connection()

    def get_speakers(self):
        # the query to execute
        sql = """select id, firstname, lastname, job, description from speaker
                 where is_active = true"""
        speakers = self.db.make_request(sql)
        # turn the list of lists returned by the database into a list of objects
        # For each list representing a speaker
        for key, speaker in enumerate(speakers):
            # instanciate a speaker object and store it in the list
            speakers[key] = Speaker(speaker)
        return speakers

    def add_speaker(self, speaker):
        # the query to execute
        sql = """insert into speaker (firstname, lastname, job, description)
                 values(%s, %s, %s, %s)"""
        message = "Nous n'avons pas pu réaliser l'enregistrement"
        arguments = (speaker.firstname, speaker.lastname, speaker.job, speaker.description)
        return self.db.make_request(sql, message=message, arguments=arguments)

    def delete_speaker(self, id):
        # the query to execute
        sql = """delete from speaker
                 where id = %s"""
        arguments = (id,)
        message = "Un problème est survenu, nous n'arrivons pas à supprimer l'intervenant d'id {}".format(id)
        return self.db.make_request(sql, arguments=arguments, message=message)
