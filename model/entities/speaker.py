# coding: utf-8

class Speaker():
    """Class representiong the user entity stored in database"""

    def __init__(self, data = False):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.job = None
        self.description = None
        self.is_active = None
        if data:
            self.hydrate(data)

    def hydrate(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
