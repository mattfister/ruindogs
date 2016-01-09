from poem import Poem
from journal_entry import Journal_Entry
import random

__author__ = "Matt Fister"


class Engraving(object):
    def __init__(self, ruin):
        if random.random() < 0.5:
            self.content = Poem(ruin)
        else:
            self.content = Journal_Entry(ruin)

    def render(self):
        self.content.render()
