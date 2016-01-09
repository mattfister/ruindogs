from freezeword import vocab
from freezeword import templates
from freezeword import md_writer
import random

__author__ = "Matt Fister"


class Poem(object):
    def __init__(self):
        self.lines = []
        self.lines.append(self.generate_opening())
        self.lines.append(self.generate_middle_line())
        while random.random() < 0.7:
            self.lines.append(self.generate_middle_line())

    def generate_opening(self):
        return (templates.Template("{{line}}")
                .render(line="{{metaphor}}|{{people}}",
                        metaphor="A {{metone}} is a {{mettwo}}",
                        metone=vocab.get_ogden_basic_noun(),
                        mettwo=vocab.get_noun(),
                        people="{{peoplephrase}} {{peopleare}}",
                        peoplephrase="We are|You are|They are|All of us are",
                        peopleare="cursed|dying|corrupted|free|joyful|sorrowful|lost|frozen|damned|hidden|love|maddened"))

    def generate_middle_line(self):
        return (templates.Template("{{line}}")
                .render(line="{{list}}|{{butphrase}}",
                        list="{{adj1}}, {{adj2}}, {{adj3}}",
                        adj1=vocab.get_adj(), adj2=vocab.get_adj(), adj3=vocab.get_adj(),
                        butphrase="{{butword}} {{adj1}}",
                        butword="yet|but|yet never|but never|ever|always"))

    def render(self):
        for line in self.lines:
            md_writer.print_quote_line(line)
