# coding: utf-8
from .connection import connection

class speakerModel():
    """Class to perform all queries related to the speaker table in the database"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        self.db = connection()
