from free_verse_poem import FreeVersePoem
from lament_poem import LamentPoem
from journal_entry import Journal_Entry
import random

__author__ = "Matt Fister"


class Engraving(object):
    def __init__(self, ruin):
        if random.random() < 0.5:
            if random.random() < 0.5:
                self.content = FreeVersePoem(ruin)
            else:
                self.content = LamentPoem(ruin)
        else:
            self.content = Journal_Entry(ruin)

    def render(self):
        self.content.render()
