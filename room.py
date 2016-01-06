from freezeword import vocab
from freezeword import templates
from freezeword import a_or_an
import random


class Room:

    def __init__(self):
        self.name = templates.Template("{{adj}} {{room}}").render(adj=vocab.get_place_adj(),
                                                                  room=vocab.get_ruin_room())

        self.name = (random.choice([a_or_an.a_or_an(self.name), 'the']) + " " + self.name).title()


if __name__ == '__main__':
    room = Room()
    print(room.name)

