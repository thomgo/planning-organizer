# coding: utf-8
from .connection import connection

class speakerModel():
    """Class to perform all queries related to the speaker table in the database"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        self.db = connection()

    def add_speaker(self, speaker):
        sql = """insert into speaker (firstname, lastname, job, description)
                 values(%s, %s, %s, %s)"""
        message = "Nous n'avons pas pu réaliser l'enregistrement"
        arguments = (speaker.firstname, speaker.lastname, speaker.job, speaker.description)
        return self.db.make_request(sql, message=message, arguments=arguments)
