from freezeword import templates

class Trap(object):
    def __init__(self):
        self.description = templates.Template("{{sentence}}").render(
            sentence="When activated, a {{trigger}} will {{trap}}.",
            trigger="tripwire|pressure plate|magical rune|magical sound detector|magical proximity detector",
            trap="launch an arrow|open a trapdoor in the floor|launch a fusillade of darts|launch a poison dart|launch a poison needle|close a portcullis"
            "|launch a rolling boulder|fire a scything blade|extend a spring loaded spear|launch a swinging block|launch a blade"
            "|launch a javelin|fire a net|open a large pit in the floor|open a large pit in the floor|swing a tripping chain"
            "|launch a ceiling pendulum|blast flames|launch a hail of needles|fire an acid arrow|launch stone blocks from the ceiling"
            "|cast a curse|collapse a column|shoot a lightning bolt|flood the room with water|launch a fireball|make the walls close in"
            "|collapse a wall|make the ceiling slowly lower|ring a bell"
        )
