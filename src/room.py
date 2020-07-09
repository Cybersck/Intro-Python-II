# Implement a class to hold room information. This should have name and
# description attributes.

class Room(object):
    def __init__(self, _id, name, description, items):
        self.id = _id
        self.name = name
        self.description = description
        self.items = items
    def __str__(self):
        return '{self.name} \n {self.description}'.format(self=self)