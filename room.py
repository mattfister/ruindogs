from freezeword import vocab
from freezeword import templates
from freezeword import a_or_an
import random
from connector import Connector
from freezeword import md_writer

__author__ = "Matt Fister"


class Room:

    def __init__(self):
        self.simple_name = vocab.get_ruin_room()
        self.adj = vocab.get_place_adj()

        self.full_name = templates.Template("the {{adj}} {{room}}").render(adj=self.adj,
                                                                  room=self.simple_name)
        self.name = ('the ' + self.simple_name)

        self.connections = {'north': None, 'south': None, 'east': None, 'west': None}
        self.opposite_directions = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}

        self.props = [vocab.get_fantasy_prop(), vocab.get_fantasy_prop()]

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
            new_connector = Connector()
            new_room = Room()
            self.connections[new_direction] = (new_connector, new_room)
            new_room.set_connection(self.opposite_directions[new_direction], (new_connector, self))
            return new_room

    def is_fully_connected(self):
        for key, val in self.connections.items():
            if val is None:
                return False
        return True

    def set_connection(self, direction, connection):
        self.connections[direction] = connection

    def render(self):
        md_writer.print_chapter_subheading(self.full_name.title())
        for prop in self.props:
            md_writer.print_list_item(templates.Template("There is {{aoran}} {{prop}} here.").render(aoran=a_or_an.a_or_an(prop), prop=prop) + "\n")
        for key, val in self.connections.items():
            if val is None:
                pass
            elif val == 'entrance':
                 md_writer.print_list_item(templates.Template("To the {{direction}} is the entrance.").render(direction=key) + "\n")
            else:
                connection = val[0]
                connected_room = val[1]
                md_writer.print_list_item(templates.Template("To the {{direction}} {{connection}} {{leadsto}} {{room}}.").render(
                    direction=key, connection=connection.description,
                    leadsto="leads to|connects to|opens to",
                    room=connected_room.full_name) + "\n")

if __name__ == '__main__':
    room = Room()
    print(room.full_name)

