# coding: utf-8
from .connection import connection

class conferenceModel():
    """Class to perform all queries related to the conference table in the database"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        self.db = connection()

    def get_conferences(self):
        try:
            self.db.initialize_connection()
            return self.db.cursor.execute(
                """
                select * from conference as c
                inner join speaker as s
                on s.id = c.speaker_id
                """
            )
        except Exception as e:
            print("Un problème est survenu, nous ne parvenons pas à récupérer les conférences")
        finally:
            self.db.close_connection()
