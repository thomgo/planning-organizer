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

    def __str__(self):
        return "~~~~~~~~~~~~~~~~~~~\nid: {}\nfirstname: {}\nlastname: {}\njob: {}\ndescription: {}\n".format(
        self.id, self.firstname, self.lastname, self.job, self.description)
