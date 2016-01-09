from poem import Poem

__author__ = "Matt Fister"


class Engraving(object):
    def __init__(self):
        self.poem = Poem()

    def render(self):
        self.poem.render()
