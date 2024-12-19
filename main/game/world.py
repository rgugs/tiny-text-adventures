class World:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.locations = []

    def set_timer(self):
        '''Sets a timer to end gameplay after a user designated time. Ask user if they want to end or continue.'''
        pass

    def load_world(self):
        '''Run self.load_world() in subclass to load the world data from a json file'''
        pass

    def show_world(self):
        '''Show information about the world when user types info <world number>'''
        print(f'{self.name} World')
        print(self.description)