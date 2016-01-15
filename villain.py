import random
import monsters
from freezeword import names
from freezeword import vocab
from freezeword import templates
from freezeword import md_writer
import ruin_race

class Villain(object):
    def __init__(self, ruin):
        self.ruin = ruin
        self.race = ruin_race.get_ruin_race()
        self.monster = monsters.get_monster(self.ruin.challenge_rating, 1, True)
        self.gender = random.choice(['male', 'female'])
        self.name = names.get_name(self.gender)
        self.quality = random.choice([vocab.get_negative_quality(), vocab.get_negative_quality()]).title()
        self.motivation_description = (templates.Template("He_or_she {{gender}} {{motivation}}.")
                                       .render(motivation="{{religion}}|{{artifact}}",
                                               religion="is founding a new religion",
                                               artifact="is trying to {{relation}} {{artifact_name}}",
                                               artifact_name=md_writer.phrase_as_link(self.ruin.artifact.name),
                                               relation="research|find|discover|understand|exploit|use|hide|destroy|steal|recover",
                                               gender=self.gender))

    def __str__(self):
        return self.name + " The " + self.quality
