from ruin import Ruin
from freezeword import md_writer
from os import listdir
from os.path import isfile, join
import random

__author__ = "Matt Fister"


if __name__ == '__main__':
    for i in range(10):
        ruin = Ruin()
        md_writer.new_file(ruin.name.replace(" ", "-"))
        ruin.render()
    only_files = [f for f in listdir(md_writer.output_folder) if isfile(join(md_writer.output_folder, f))]
    md_writer.new_file('index')
    random.shuffle(only_files)
    md_writer.print_title("Ruin Dogs")
    md_writer.print_sub_title("V2 - Ruin Index")
    for file in only_files:

        if file.endswith('.html') and file != 'index.html':
            ruin_name = file.split('.html')[0].replace('-',' ').title()
            md_writer.print_chapter_heading(md_writer.phrase_with_link(ruin_name, '../'+md_writer.output_folder+'/'+file))
    md_writer.end_novel(css='http://mattfister.github.io/ruindogs/base.css')
