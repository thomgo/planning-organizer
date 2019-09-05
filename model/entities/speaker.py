# coding: utf-8

from .entity import Entity

class Speaker(Entity):
    """Class representiong the user entity stored in database"""

    def __init__(self, data = False):
        super().__init__()
        self.firstname = None
        self.lastname = None
        self.job = None
        self.description = None
        self.is_active = None
        if data:
            self.hydrate(data)


    def __str__(self):
        return "~~~~~~~~~~~~~~~~~~~\nid: {}\nfirstname: {}\nlastname: {}\njob: {}\ndescription: {}\n".format(
        self.id, self.firstname, self.lastname, self.job, self.description)
