# coding: utf-8

class Entity():
    """Class representing the mother entity class"""

    def __init__(self, data = False):
        self.id = None

    def hydrate(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
