from freezeword import vocab
from freezeword import templates
from freezeword import a_or_an
import random
from connector import Connector
from freezeword import md_writer
from engraving import Engraving
from enemy import Enemy
from freezeword import write_out_list

__author__ = "Matt Fister"


class Room:

    def __init__(self, ruin):
        self.ruin = ruin
        self.simple_name = vocab.get_ruin_room()
        self.adj = vocab.get_place_adj()

        self.full_name = templates.Template("the {{adj}} {{room}}").render(adj=self.adj,
                                                                  room=self.simple_name)
        self.name = ('the ' + self.simple_name)

        self.details = []

        self.enemies = []
        while random.random() < 0.5:
            self.enemies.append(Enemy(ruin))

        if len(self.enemies) > 0:
            self.details.append(self.generate_enemy_description())

        if random.random() < 0.5:
            self.details.append(self.generate_flora_description())

        if random.random() < 0.5:
            self.details.append(self.generate_atmosphere_description())

        if random.random() < 0.5:
            self.details.append(self.generate_walls_description())

        if random.random() < 0.5:
            self.details.append(self.generate_floor_description())



        random.shuffle(self.details)

        self.connections = {'north': None, 'south': None, 'east': None, 'west': None}
        self.opposite_directions = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}

        self.props = []
        while random.random() < 0.25:
            self.props.append(vocab.get_fantasy_prop())

        self.north = None
        self.south = None
        self.east = None
        self.west = None

        self.artifact = None
        self.villain = None

        self.engraving_location = random.choice(["the wall","the floor","the ceiling","a monolith","a tablet","a stone"])

        self.engraving = None
        if random.random() < 0.25:
            self.engraving = Engraving(self.ruin)

    def generate_enemy_description(self):
        if len(self.enemies) > 1:
            return "There are " + write_out_list.write_out_list(self.enemies, False) + " here."
        else:
            return "There is " + self.enemies[0].__str__() + " are here."

    def generate_flora_description(self):
        return templates.Template("{{sentence}}").render(sentence="{{growsentence}}",
                                                      growsentence="{{plantphrase}} {{grow}} {{plantlocation}}.",
                                                          plantphrase="{{color}} {{plant}}",
                                                      plant="razorgrass is|mushrooms are|moss is|lichens are|ferns are",
                                                      color="Red|Green|Yellow|Blue|Gray|White",
                                                      grow="growing|sprouting|decaying|swaying",
                                                      plantlocation="in cracks in the floor|in broken urns|in a patch on the floor|from the walls|from the ceiling")

    def generate_atmosphere_description(self):
        return (templates.Template("{{sentence}}")
                .render(sentence="The air {{smells_or_tastes}} {{smell}} here.",
                        smells_or_tastes="smells|tastes|seems",
                        smell="salty|like ozone|like bloody|musty|dry|magically charged|humid|nauseating|poisonous|sticky"))

    def generate_walls_description(self):
        return (templates.Template("{{sentence}}")
                .render(sentence="The {{material}} walls are {{descriptor}}.",
                        material="brick|wooden|stone|concrete|crystal|glass|obsidion|metallic|mirrored",
                        descriptor="pristine|ruined|scratched|caving in|unsettled|bloodstained|covered in mold"))

    def generate_floor_description(self):
        return (templates.Template("{{sentence}}")
                .render(sentence="The floor is {{floor_phrase}}.",
                        floor_phrase="flooded with {{number}} inch deep {{temp}} water|sticky|bloodstained|cluttered with {{clutter}}|smooth|glossy",
                        number="one|two|three|four|five|six|seven|eight|nine",
                        temp="cold|cool|lukewarm|hot|scalding",
                        clutter="debris|bones|rocks|shells|broken glass|ashes"))

    def add_connected_room(self):
        if self.is_fully_connected():
            return None
        else:
            empty_connections = {}
            for key, value in self.connections.items():
                if value is None:
                    empty_connections[key] = value
            new_direction = random.choice(list(empty_connections.keys()))
            new_connector = Connector()
            new_room = Room(self.ruin)
            self.connections[new_direction] = (new_connector, new_room)
            new_room.set_connection(self.opposite_directions[new_direction], (new_connector, self))
            return new_room

    def is_fully_connected(self):
        for key, val in self.connections.items():
            if val is None:
                return False
        return True

    def set_connection(self, direction, connection):
        self.connections[direction] = connection

    def render(self):
        md_writer.print_chapter_subheading(md_writer.phrase_with_anchor(self.full_name))

        for sentence in self.details:
            md_writer.print_chapter_sentence(sentence)

        md_writer.end_chapter()

        if self.engraving is not None:
            md_writer.print_chapter_sentence(templates.Template("There is an engraving on {{location}} written in {{language}}.")
                                             .render(location=self.engraving_location,
                                                     language=self.ruin.race.name + " Script|common"))
            md_writer.end_paragraph()
            self.engraving.render()
        md_writer.end_chapter()

        for prop in self.props:
            md_writer.print_list_item(templates.Template("There is a_or_an {{prop}} here.").render(prop=prop) + "\n")
        if self.artifact is not None:
            md_writer.print_list_item(templates.Template("{{artifact}} is here.").render(artifact=md_writer.phrase_as_link(self.artifact.name)) + "\n")
        if self.villain is not None:
            md_writer.print_list_item(templates.Template("{{villain}} is here.").render(villain=md_writer.phrase_as_link(self.villain.__str__())) + "\n")

        for key, val in self.connections.items():
            if val is None:
                pass
            elif val == 'entrance':
                 md_writer.print_list_item(templates.Template("To the {{direction}} is the entrance.").render(direction=key) + "\n")
            else:
                connection = val[0]
                connected_room = val[1]
                md_writer.print_list_item(templates.Template("To the {{direction}} {{connection}} {{leadsto}} {{room}}.\n").render(
                    direction=key, connection=connection.description,
                    leadsto="leads to|connects to|opens to",
                    room="["+connected_room.full_name+"]"+"(#"+connected_room.full_name.replace(" ","-")+")"))


