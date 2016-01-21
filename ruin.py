from room import Room
from villain import Villain
from artifact import Artifact
from random import choice
import random
from freezeword import old_language_generator
from freezeword import templates
from freezeword import md_writer
from freezeword import vocab
import monsters
import ruin_race
import grapher

__author__ = "Matt Fister"


class Ruin(object):
    def __init__(self):

        self.challenge_rating = random.randint(2, 10)

        self.name = (templates.Template("{{output}}")
                     .render(output="{{old1}}|{{old1}} {{old2}}|The {{adj}} {{noun}}",
                             old1=old_language_generator.random_word(),
                             old2=old_language_generator.random_word(),
                             adj=vocab.get_adj(),
                             noun=vocab.get_noun()).title())

        self.location_description = templates.Template('{{sentence}}').render(sentence="{{name}} is {{locationphrase}} {{placement}}.",
                                                         name=self.name.title(),
                                                         locationphrase="located in|located on|constructed on|located under",
                                                         placement="a_or_an {{adj}} tree|a_or_an {{adj}} plain|a_or_an {{adj}} city|a_or_an {{adj}} rift|a_or_an {{adj}} mountain",
                                                         adj="alien|obsidion|crystal|spikey|giant|flooded|ruined|volcanic|cursed|poisoned|haunted|broken")

        self.parts_description = (templates.Template('{{sentence}}')
                                  .render(sentence="{{segment}} of {{name}} are {{state}}.",
                                          segment="Parts|Some areas|Regions|Some rooms",
                                          name=self.name.title()+"|it",
                                          state="cursed|corrupted|flooded|{{adj}} hot|{{adj}} cold|frozen|foggy|inaccessible|flooded",
                                          adj="incredibly|somewhat|unbearably"))

        self.circumstances_description = (templates.Template('{{sentence}}')
                                          .render(sentence="A_or_an {{outside_thing}} is happening outside.|The ruin is {{ruin_becoming}}.",
                                                  outside_thing="massive storm|battle between raiders|solar eclipse|massive flood|windstorm|blizzard|lunar eclipse",
                                                  ruin_becoming="flooding|coming to life|sinking into the earth|collapsing slowly|burning|larger on the inside than the outside"))

        self.artifact = Artifact()

        self.race = monsters.get_race(self.challenge_rating)
        self.race_description = (templates.Template('{{sentence}}')
                                 .render(sentence="It is occupied by {{plural_race}}.",
                                         plural_race=self.race))

        self.villain = Villain(self)

        self.villain_sentence = (templates.Template('{{sentence}}')
                                 .render(sentence="{{villain}}, a_or_an {{villain_type}} is here.",
                                         villain=md_writer.phrase_with_anchor(self.villain.__str__()),
                                         villain_type=self.villain.monster.name))

        self.race_villain_relation_sentence = (templates.Template("{{sentence}}")
                                               .render(sentence="The {{race_name}} {{relation}} {{villain}}.",
                                                       race_name=self.race,
                                                       relation="are the slaves of|have been charmed by|are ruled by|worship|are the minions of|are the soldiers of|are battling",
                                                       villain=self.villain.__str__()))

        self.entrance = Room(self)
        self.entrance.set_connection('south', 'entrance')

        self.rooms = [self.entrance]

        rooms_to_build = random.randint(5, 15)
        while len(self.rooms) < rooms_to_build:
            random_room = choice(self.rooms)
            new_room = random_room.add_connected_room()
            if new_room is not None:
                self.rooms.append(new_room)

        random_room.artifact = self.artifact
        random_room = choice(self.rooms)
        random_room.villain = self.villain

    def room_in_position(self, pos):
        for room in self.rooms:
            if pos[0] == 0 and pos[1] == -1:
                return True
            if pos[0] == room.pos[0] and pos[1] == room.pos[1]:
                return True
        return False

    def render(self):
        ruin_save_name = self.name.replace(" ", "-")
        ruin_map_file_name = ruin_save_name + ".png"
        grapher.save_graph(self, ruin_map_file_name)
        md_writer.print_title("Ruin Dogs")
        md_writer.print_sub_title(self.name)
        md_writer.print_chapter_heading("Overview")
        md_writer.print_chapter_sentence(self.location_description)
        md_writer.print_chapter_sentence(self.parts_description)
        md_writer.print_chapter_sentence(self.circumstances_description)
        md_writer.print_chapter_sentence(self.race_description)
        md_writer.print_chapter_sentence(self.villain_sentence)
        md_writer.print_chapter_sentence(self.race_villain_relation_sentence)
        md_writer.print_chapter_sentence(self.villain.motivation_description)
        md_writer.end_paragraph()
        md_writer.end_chapter()
        md_writer.print_chapter_heading("Artifact")
        self.artifact.render()
        md_writer.end_paragraph()
        md_writer.end_chapter()
        md_writer.print_chapter_heading("Locations")
        md_writer.end_chapter()
        md_writer.insert_image('../'+md_writer.output_folder+'/images/' + ruin_map_file_name, 'layout')
        for room in self.rooms:
            room.render()
            md_writer.end_paragraph()
        md_writer.end_novel(css='http://mattfister.github.io/ruindogs/base.css')


if __name__ == '__main__':
    ruin = Ruin()
    ruin.render()
