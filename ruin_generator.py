from ruin import Ruin
from freezeword import md_writer
from os import listdir
from os.path import isfile, join
import random

__author__ = "Matt Fister"


if __name__ == '__main__':
    for i in range(100):
        ruin = Ruin()
        md_writer.new_file(ruin.name.replace(" ", "-"))
        ruin.render()
    only_files = [f for f in listdir('output') if isfile(join('output', f))]
    md_writer.new_file('index')
    random.shuffle(only_files)
    for file in only_files:
        if file.endswith('.html') and file != 'index.html':
            ruin_name = file.split('.html')[0].replace('-',' ').title()
            md_writer.print_chapter_heading(md_writer.phrase_with_link(ruin_name, '../output/'+file))
    md_writer.end_novel(css='http://mattfister.github.io/ruindogs/base.css')
