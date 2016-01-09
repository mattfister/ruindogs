from freezeword import vocab
from freezeword import templates
from freezeword import md_writer
import random

__author__ = "Matt Fister"


class Poem(object):
    def __init__(self, ruin):
        self.ruin = ruin
        self.lines = []
        opening_line = self.generate_opening()
        self.lines.append(opening_line)
        self.lines.append(self.generate_middle_line())
        while random.random() < 0.7:
            if random.random() < 0.3:
                self.lines.append(self.generate_opening())
            self.lines.append(self.generate_middle_line())

        if (random.random() < 0.5):
            if (random.random() < 0.5):
                self.lines.append(opening_line)
            else:
                self.lines.append(self.generate_end_line())

    def generate_opening(self):
        artifact_name = md_writer.phrase_as_link(self.ruin.artifact.name)
        return (templates.Template("{{line}}")
                .render(line="{{metaphor}}|{{people}}|{{artifact}}|{{lament}}",
                        artifact=artifact_name,
                        metaphor="A_or_an {{metone}} is a_or_an {{mettwo}}",
                        lament="{{poor_word}} {{poor_verb}} {{object}}",
                        poor_word="O!|O|Oh|Poor|Dear|My",
                        poor_verb="sorry|sad|pitiful|cruel|weak|meak|terrible|dire",
                        object="world|us|you|we|fate|cruelty|suffering|sadness|coldness|stars",
                        metone=vocab.get_ogden_basic_noun(),
                        mettwo=vocab.get_noun(),
                        people="{{peoplephrase}} {{peopleare}}",
                        peoplephrase="We are|You are|They are|All of us are",
                        peopleare="cursed|dying|corrupted|free|joyful|sorrowful|lost|frozen|damned|hidden|love|maddened|envious"))

    def generate_middle_line(self):
        return (templates.Template("{{line}}")
                .render(line="{{list}}|{{list2}}|{{butphrase}}",
                        list="{{adj1}}, {{adj2}}, {{adj3}}",
                        list2="{{adj1}} and {{adj2}}",
                        adj1=vocab.get_adj(), adj2=vocab.get_adj(), adj3=vocab.get_adj(),
                        butphrase="{{butword}} {{adj1}}",
                        butword="yet|but|yet never|but never|ever|always"))

    def generate_end_line(self):
        return (templates.Template("{{line}}")
                .render(line="{{youline}}",
                        youline="you {{verb_phrase}} {{noun}}",
                        verb_phrase="must be|will be|shall be|must never be|are not|are",
                        noun="destroyed|cursed|eaten|consumed|loved|captured|frozen|punished|hidden|joined|crystalized|remembered|returned"))


    def render(self):
        for line in self.lines:
            md_writer.print_quote_line(line)
