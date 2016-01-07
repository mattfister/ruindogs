from freezeword import vocab
from freezeword import templates
from freezeword import a_or_an
import random


class Room:

    def __init__(self):
        self.simple_name = vocab.get_ruin_room()
        self.adj = vocab.get_place_adj()

        self.full_name = templates.Template("the {{adj}} {{room}}").render(adj=self.adj,
                                                                  room=self.simple_name)
        self.name = ('the ' + self.simple_name)

        self.connections = {'north': None, 'south': None, 'east': None, 'west': None}

        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def add_connected_room(self):
        if self.is_fully_connected():
            return None
        else:
            empty_connections = {}
            for key, value in self.connections.items():
                if value is None:
                    empty_connections[key] = value
            new_direction = random.choice(list(empty_connections.keys()))
            new_room = Room()
            self.connections[new_direction] = new_room
            return new_room


    def is_fully_connected(self):
        for key, val in self.connections.items():
            if val is None:
                return False
        return True

    def set_connection(self, direction, connection):
        self.connections[direction] = connection

if __name__ == '__main__':
    room = Room()
    print(room.full_name)

