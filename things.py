from abc import ABC

class Thing(ABC):
    def __init__(self, name, description, type, getable=False, location=(0,0)):
        self.name = name
        self.description = description
        self.location = location
        self.type = type
        self.getable = getable

class Inventory:
    def __init__(self):
        self.inventory = []

class Container(Thing):
    def __init__(self, name, description, type, getable=False, location=(0, 0)):
        super().__init__(name, description, type, getable, location)
        self.inventory = Inventory()
        
class Actor(Thing):
    def __init__(self, name, description, type, getable=False, location=(0, 0)):
        super().__init__(name, description, type, getable, location)
        self.inventory = Inventory()
        self.is_alive = True