# Implement a class to hold room information. This should have name and
# description attributes.

class Room(object):
    def __init__(self, key, name, description):
        self.key = key
        self.name = name
        self.description = description
    def __str__(self):
        return '{self.name} \n {self.description}'.format(self=self)