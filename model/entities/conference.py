# coding: utf-8
from .entity import Entity

class Conference():
    """Class representiong the conference entity stored in database"""

    def __init__(self, data=False):
        super().init()
        self.title = None
        self.summary = None
        self.event_date = None
        self.registering_date = None
        self.event_time = None
        self.speaker = None
        if data:
            self.hydrate(data)
