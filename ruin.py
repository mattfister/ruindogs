from room import Room
from random import choice
from freezeword import old_language_generator
from freezeword import templates
__author__ = "Matt Fister"


class Ruin(object):
    def __init__(self):
        self.name = templates.Template("The Ruin {{output}}").render(output="{{wordone}}|{{wordone}} {{wordtwo}}", wordone=old_language_generator.random_word(), wordtwo=old_language_generator.random_word()).title()
        self.entrance = Room()
        self.entrance.set_connection('south', 'entrance')

        self.rooms = [self.entrance]

        rooms_to_build = 5
        while len(self.rooms) < rooms_to_build:
            random_room = choice(self.rooms)
            new_room = random_room.add_connected_room()
            if new_room is not None:
                self.rooms.append(new_room)

    def __str__(self):
        ret_str = self.name + "\n"
        for room in self.rooms:
            ret_str += room.__str__() + "\n"
        return ret_str