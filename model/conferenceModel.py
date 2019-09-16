# coding: utf-8
from .connection import connection

class conferenceModel():
    """Class to perform all queries related to the conference table in the database"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        self.db = connection()

    def get_conferences(self):
        sql ="select * from conference as c inner join speaker as s on s.id = c.speaker_id"
        return self.db.make_request(sql)

    def add_conference(self, conference):
        sql = """insert into conference(title, summary, event_date, registering_date, event_time, speaker_id)
                 values(%s, %s, %s, now(), %s, %s)"""
        arguments = (conference.title, conference.summary, conference.event_date, conference.event_time, conference.speaker)
        # message=  "Nous n'avons pas pu enregistrer la conférence, un problème est survenu"
        return self.db.make_request(sql, arguments=arguments)
