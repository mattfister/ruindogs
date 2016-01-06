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


if __name__ == '__main__':
    room = Room()
    print(room.full_name)

