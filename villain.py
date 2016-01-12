import random
from freezeword import a_or_an
from freezeword import names
from freezeword import vocab
import ruin_race

class Villain(object):
    def __init__(self, ruin):
        self.ruin = ruin
        self.race = ruin_race.get_ruin_race()
        self.job = random.choice(ruin.race.classes)
        self.gender = random.choice(['male', 'female'])
        self.name = names.get_name(self.gender)
        self.quality = random.choice([vocab.get_negative_quality(), vocab.get_negative_quality()]).title()

    def __str__(self):
        return a_or_an.a_or_an(self.race.name) + ' ' + self.race.name + ' ' + self.job
