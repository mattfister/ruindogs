from room import Room
from random import choice
from freezeword import old_language_generator
from freezeword import templates
from freezeword import md_writer


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

    def render(self):
        md_writer.print_title("Ruin Dogs")
        md_writer.print_sub_title(self.name)
        md_writer.print_title("Locations")
        for room in self.rooms:
            room.render()
            md_writer.end_paragraph()
        md_writer.end_novel(css='https://mattfister.github.io/nanogenmo2015/samples/base.css')
