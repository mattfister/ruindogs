import random
from freezeword import a_or_an

class Enemy(object):
    def __init__(self, ruin):
        self.ruin = ruin
        self.race = ruin.race.name
        self.job = random.choice(ruin.race.classes)

    def __str__(self):
        return a_or_an.a_or_an(self.race) + ' ' + self.race + ' ' + self.job
