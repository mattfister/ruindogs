from freezeword import old_language_generator
from freezeword import templates
from freezeword import vocab
from freezeword import md_writer

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

        self.when_sentence = (templates.Template("When {{action}} it {{transition}} {{ending}}.")
                              .render(action="gazed upon|touched|picked up|smelled|tasted|eaten|worn|carried|held|cradled|rubbed|thrown",
                                      transition="seems like it begins to|begins to",
                                      ending="become hot|become energized with a powerful vibration|liquify|glow with an eerie light|dissappear|"
                                             "show an image of the future|become a shielding force|an aid to memory|become a deadly projectile|"
                                             "repel insects|frighten children|become a force of destiny|become lost|burn the mind|sing the hymn of the damned|"
                                             "curse all nearby|illuminate its surroundings"))
    def render(self):
        md_writer.print_chapter_subheading('<a name="' + self.name.replace(" ", "-") + '"></a>'+self.name)
        md_writer.end_chapter()
        md_writer.print_chapter_sentence(self.form)
        md_writer.print_chapter_sentence(self.when_sentence)
        md_writer.end_chapter()


