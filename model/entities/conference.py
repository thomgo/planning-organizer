# coding: utf-8
import datetime

from .entity import Entity

class Conference(Entity):
    """Class inheriting from entity representing the conferences stored in database"""

    def __init__(self, data=False):
        # call the mother class constructor
        super().__init__()
        self.title = None
        self.summary = None
        self.event_date = None
        self.registering_date = None
        self.event_time = None
        self.speaker = None
        # if there is a dictionnary the hydrate the object
        if data:
            self.hydrate(data)

    def __str__(self):
        """Define the way the object is printed"""
        return "~~~~~~~~~~~~~~~~~~~\nid: {}\ntitle: {}\nsummary: {}\ndate: {}\nhour: {}\nspeaker: {}\n".format(
            self.id,
            self.title,
            self.summary,
            self.event_date.strftime("%d/%m/%Y"),
            self.event_time.strftime("%H:%M"),
            self.speaker.firstname + " " + self.speaker.lastname
        )
