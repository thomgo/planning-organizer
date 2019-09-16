# coding: utf-8
import datetime

from .entity import Entity

class Conference(Entity):
    """Class representing the conference entity stored in database"""

    def __init__(self, data=False):
        super().__init__()
        self.title = None
        self.summary = None
        self.event_date = None
        self.registering_date = None
        self.event_time = None
        self.speaker = None
        if data:
            self.hydrate(data)

    def __str__(self):
        return "~~~~~~~~~~~~~~~~~~~\nid: {}\ntitle: {}\nsummary: {}\ndate: {}\nhour: {}\n".format(
        self.id, self.title, self.summary, self.event_date.strftime("%d/%m/%Y"), self.event_time.strftime("%H:%M"))
