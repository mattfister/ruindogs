from room import Room
from villain import Villain
from artifact import Artifact
from random import choice
from freezeword import old_language_generator
from freezeword import templates
from freezeword import md_writer
from freezeword import vocab
import ruin_race

__author__ = "Matt Fister"


class Ruin(object):
    def __init__(self):
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

        self.artifact = Artifact()

        self.race = ruin_race.get_ruin_race()
        self.race_description = (templates.Template('{{sentence}}')
                                 .render(sentence="It is occupied by {{plural_race}}.",
                                         plural_race=self.race.plural_name))

        self.villain = Villain(self)

        self.villain_sentence = (templates.Template('{{sentence}}')
                                 .render(sentence="{{name}} The {{quality}}, a_or_an {{race}} {{job}} is here.",
                                         name=self.villain.name,
                                         quality=self.villain.quality,
                                         race=self.villain.race.name,
                                         job=self.villain.job))

        self.race_villain_relation_sentence = (templates.Template("{{sentence}}")
                                               .render(sentence="The {{race_name}} {{relation}} {{villain_name}} The {{quality}}.",
                                                       race_name=self.race.plural_name,
                                                       relation="are the slaves of|have been charmed by|are ruled by|worship|are the minions of|are the soldiers of|are battling",
                                                       villain_name=self.villain.name,
                                                       quality=self.villain.quality))

        self.entrance = Room(self)
        self.entrance.set_connection('south', 'entrance')

        self.rooms = [self.entrance]


        rooms_to_build = 10
        while len(self.rooms) < rooms_to_build:
            random_room = choice(self.rooms)
            new_room = random_room.add_connected_room()
            if new_room is not None:
                self.rooms.append(new_room)

        random_room.artifact = self.artifact

    def render(self):
        md_writer.print_title("Ruin Dogs")
        md_writer.print_sub_title(self.name)
        md_writer.print_chapter_heading("Overview")
        md_writer.print_chapter_sentence(self.location_description)
        md_writer.print_chapter_sentence(self.parts_description)
        md_writer.print_chapter_sentence(self.race_description)
        md_writer.print_chapter_sentence(self.villain_sentence)
        md_writer.print_chapter_sentence(self.race_villain_relation_sentence)
        md_writer.end_paragraph()
        md_writer.end_chapter()
        md_writer.print_chapter_heading("Artifact")
        self.artifact.render()
        md_writer.end_paragraph()
        md_writer.end_chapter()
        md_writer.print_chapter_heading("Locations")
        md_writer.end_chapter()
        for room in self.rooms:
            room.render()
            md_writer.end_paragraph()
        md_writer.end_novel(css='https://mattfister.github.io/ruindogs/base.css')
