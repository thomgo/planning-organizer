# coding: utf-8

from .entity import Entity

class Speaker(Entity):
    """Class inheriting from entity representiong the speakers stored in database"""

    def __init__(self, data = False):
        # call the mother class constructor
        super().__init__()
        self.firstname = None
        self.lastname = None
        self.job = None
        self.description = None
        self.is_active = None
        # if there is a dictionnary the hydrate the object
        if data:
            self.hydrate(data)


    def __str__(self):
        """Define the way the object is printed"""
        return "~~~~~~~~~~~~~~~~~~~\nid: {}\nfirstname: {}\nlastname: {}\njob: {}\ndescription: {}\n".format(
        self.id, self.firstname, self.lastname, self.job, self.description)
