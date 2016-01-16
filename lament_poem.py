from freezeword import vocab
from freezeword import templates
from freezeword import md_writer
import random

__author__ = "Matt Fister"


class LamentPoem(object):
    def __init__(self, ruin):
        self.ruin = ruin
        self.lines = []
        rhyme_structure = random.choice(['abab', 'aabb', 'rubaiyat'])

        while len(self.lines) == 0:
            try:
                if rhyme_structure == 'abab':
                    first_four = self.gen_first_four_lines_a_b_a_b()
                elif rhyme_structure == 'rubaiyat':
                    first_four = self.gen_first_four_lines_rubaiyat()
                else:
                    first_four = self.gen_first_four_lines_a_a_b_b()
                self.lines = self.lines + first_four
            except ValueError:
                pass

    def gen_first_four_lines_a_b_a_b(self):
        ret_lines = []
        opening_line = self.generate_opening()
        ret_lines.append(opening_line)
        ret_lines.append(self.generate_middle_line(None))

        rhymeA = ret_lines[0].rsplit(None, 1)[-1]
        rhymeB = ret_lines[1].rsplit(None, 1)[-1]

        ret_lines.append(self.generate_middle_line(rhymeA))
        ret_lines.append(self.generate_end_line(rhymeB))
        return ret_lines

    def gen_first_four_lines_a_a_b_b(self):
        ret_lines = []
        opening_line = self.generate_opening()
        ret_lines.append(opening_line)

        rhymeA = ret_lines[0].rsplit(None, 1)[-1]
        ret_lines.append(self.generate_middle_line(rhymeA))

        ret_lines.append(self.generate_middle_line(None))

        rhymeB = ret_lines[2].rsplit(None, 1)[-1]
        ret_lines.append(self.generate_end_line(rhymeB))

        return ret_lines

    def gen_first_four_lines_rubaiyat(self):
        ret_lines = []
        opening_line = self.generate_opening()
        ret_lines.append(opening_line)

        rhymeA = ret_lines[0].rsplit(None, 1)[-1]
        ret_lines.append(self.generate_middle_line(rhymeA))

        ret_lines.append(self.generate_middle_line(None))

        ret_lines.append(self.generate_end_line(rhymeA))

        return ret_lines

    def generate_opening(self):
        return (templates.Template("{{line}}")
                .render(line="{{lament}}",
                        lament="{{poor_word}} {{poor_phrase}}",
                        poor_phrase="{{poor_verb}} {{object}}|{{poor_subject}} {{poor_statement}}",
                        poor_subject="the memory of you|the world|my life|my fate|our fate|life|death|everything",
                        poor_statement="is misery|is sorrow|gives me depression|is gloom|is grief|is woe|is desolate|is dejection|is melancholy|is wickedness|is savagery|is inhumane|is brutish|is sadistic|is wickedness|is mournful|is sadness|is empty|is poor|is cruel|is hopeless|is nothing|is darkness|is death",
                        poor_word="O!|O|Oh|Poor me!|Dear me!|Oh my!",
                        poor_verb="sorry|sad|pitiful|cruel|weak|meak|terrible|dire",
                        object="world|life|destiny|soul|spirit|existence|being|prophecy|god|you|we|fate|cruelty|suffering|sadness|coldness|stars"))

    def generate_middle_line(self, rhyme):
        last_word = vocab.get_adj()
        if rhyme is not None:
            last_word_choices = vocab.rhyming_adjs(rhyme)
            if len(last_word_choices) == 0:
                raise ValueError
            last_word = random.choice(last_word_choices)


        return (templates.Template("{{line}}")
                .render(line="{{list}}|{{list2}}|{{butphrase}}|{{it_phrase}}",
                        it_phrase="it is {{always_never}} {{last_adj}}",
                        always_never = "always|never",
                        list="{{adj1}}, {{adj2}}, {{last_adj}}",
                        list2="{{adj1}} and {{last_adj}}",
                        adj1=vocab.get_adj(), adj2=vocab.get_adj(), last_adj=last_word,
                        butphrase="{{butword}} {{last_adj}}",
                        butword="yet|but|yet never|but never|ever|always"))

    def generate_end_line(self, rhyme):
        last_word = vocab.get_adj()
        if rhyme is not None:
            last_word_choices = vocab.rhyming_adjs(rhyme)
            if len(last_word_choices) == 0:
                raise ValueError
            last_word = random.choice(last_word_choices)
        return (templates.Template("{{line}}")
                .render(line="{{statement}}",
                        statement="{{subject}} is {{adj}}",
                        subject="all|sadness|cruelty|fate|the world|life|death|hope|nothing|everything",
                        adj=last_word))

    def render(self):
        for line in self.lines:
            md_writer.print_quote_line(line)


if __name__ == '__main__':
    for i in range(20):
        lament = LamentPoem(None)
        for line in lament.lines:
            print(line)