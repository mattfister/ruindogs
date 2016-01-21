from freezeword import old_language_generator
from freezeword import templates
from freezeword import vocab
from freezeword import md_writer
import random

class Artifact(object):
    def __init__(self):
        self.name = (templates.Template("{{output}}")
                     .render(output="{{old1}}|{{old1}} {{old2}}|The {{adj}} {{noun}}",
                             old1=old_language_generator.random_word(),
                             old2=old_language_generator.random_word(),
                             adj=vocab.get_adj(),
                             noun=vocab.get_noun()).title())

        self.form = (templates.Template("{{name}} {{shapephrase}} a_or_an {{adj}} {{shape}}.")
                     .render(name=self.name,
                             shapephrase="has the form of|is a powerful artifact in the shape of|looks like",
                             adj="broken|smooth|warm|cold|sharp|wet|soft|hard|mushy|transparent|glassy|opaque",
                             shape="rock|doll|figurine|amulet|orb|gem|crystal|sphere|cube|prism|blade|spear|monument|meteorite"))

        self.description_sentences = []
        if random.random() < 0.5:
            self.description_sentences.append(templates.Template("{{thing}} {{verbs}} {{direction}} it.")
                                              .render(thing="light|water|gravity|air|psychic energy|magic|cacophony|power|fire",
                                                      verbs="bends|shifts|flows|pours|incinerates|glows|slides|slips",
                                                      direction="towards|from|away from|around|near").capitalize())

        if random.random() < 0.5:
            self.description_sentences.append(templates.Template("It is a {{adj}} {{color}} color.")
                                              .render(adj="sickly|pale|bright|dark|medium|light|shifting",
                                                      color=vocab.basic_colors))

        if random.random() < 0.5:
            self.description_sentences.append(templates.Template("It smells like {{scent}}.")
                                              .render(scent=vocab.scents))

        random.shuffle(self.description_sentences)

        self.when_sentence = (templates.Template("When {{action}} {{transition}} {{ending}}.")
                              .render(action="worshipped|gazed upon|touched|picked up|smelled|eaten|worn|carried|held|cradled|rubbed|thrown",
                                      transition="it",
                                      ending="becomes hot|become energized with a powerful vibration|liquifies|glows with an eerie light|dissappears|"
                                             "shows an image of the future|becomes a shielding force|aids memory|becomes a deadly projectile|projects energy|tunnels into the earth|"
                                             "repels insects|frightens children|becomes a force of destiny|becomes lost|burns the mind|sings the hymn of the damned|"
                                             "curses all nearby|illuminates its surroundings|destroys itself|destroys others|flies into the air|floats in the air|floats above the ground|"
                                             "levitates surrounding objects|levitates those nearby|grants power to its owner|makes its owner invisible|grants a wish|"
                                             "emits dust|turns surrounding objects to ashes|ignites its surrroundings|grants psychic powers|changes the past|changes probabilities"))

    def render(self):
        md_writer.print_chapter_subheading(md_writer.phrase_with_anchor(self.name))
        md_writer.end_chapter()
        md_writer.print_chapter_sentence(self.form)
        for sentence in self.description_sentences:
            md_writer.print_chapter_sentence(sentence)
        md_writer.print_chapter_sentence(self.when_sentence)
        md_writer.end_chapter()


