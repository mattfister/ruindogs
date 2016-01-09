from freezeword import templates
import random
from freezeword import md_writer
from freezeword import old_language_generator

__author__ = "Matt Fister"

class Journal_Entry(object):
    def __init__(self, ruin):
        self.lines = []

        room_name = 'this place'
        try:
            md_writer.phrase_as_link(random.choice(ruin.rooms).full_name)
        except AttributeError:
            pass

        if random.random() < 0.5:
            self.lines.append(templates.Template("I {{verb_phrase}}.")
                              .render(verb_phrase="{{place_phrase}} {{place}}|{{artifact_verb}} {{artifact}}|am lost in {{this_place}}|am {{state}}",
                                      place="{{ruin_name}}|{{room_name}}",
                                      this_place="{{ruin_name}}",
                                      state="old|young|free|starving|afraid|powerful|a coward|alone|lonely|lost|sneaky|the best|cruel|lovely|hidden",
                                      ruin_name=ruin.name,
                                      artifact=md_writer.phrase_as_link(ruin.artifact.name),
                                      room_name=room_name,
                                      artifact_verb="found|lost|discovered|am seeking|can not find|want to find|worship",
                                      place_phrase="discovered|found|am looting|am defending|am hiding in|am worshipping|am fleeing"))

        if random.random() < 0.5:
            self.lines.append(self.generate_advice())

        if len(self.lines) == 0:
            self.lines.append(old_language_generator.random_word().title() + " "
                              + old_language_generator.random_word() + " "
                              + old_language_generator.random_word() + " "
                              + old_language_generator.random_word() + " "
                              + old_language_generator.random_word() + ".")


    def generate_advice(self):
        return templates.Template("{{advice}}.").render(
            advice="{{advice_verb}} {{advice_gerund}}",
            advice_verb="Try|Maybe try|Do not try|I tried|I could not try|I thought about",
            advice_gerund="digging|hiding|running|leaving|jumping|swimming|cowering|praying|fighting|dying|giving up"
        )

    def render(self):
        for line in self.lines:
            md_writer.print_quote_line(line)