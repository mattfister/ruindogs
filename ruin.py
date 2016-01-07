from room import Room
from random import choice

class Ruin(object):
    def __init__(self):
        self.entrance = Room()
        self.entrance.south = 'entrance'

        self.rooms = [self.entrance]

        rooms_to_build = 5
        while len(self.rooms) < rooms_to_build:
            random_room = choice(self.rooms)
            new_room = random_room.add_connected_room()
            if new_room is not None:
                self.rooms.append(new_room)


        for room in self.rooms:
            print(room.full_name)
