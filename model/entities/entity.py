# coding: utf-8

class Entity():
    """Class representing the mother entity class"""

    def __init__(self, data = False):
        # every entity must have an ID
        self.id = None

    def hydrate(self, data):
        """Set object's attributs value if they exists from a dictionnary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
