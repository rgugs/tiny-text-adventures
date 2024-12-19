class Player:
    def __init__(self, name):
        self.name = name
        self.current_world = None
        self.active = True

    def enter_world(self, world):
        self.current_world = world
        print(f"{self.name} has entered {world.name}.")
        world.show_world_info()

        