from freezeword import templates
from freezeword import a_or_an
from freezeword import vocab


class Connector(object):

    def __init__(self):
        self.description = templates.Template("{{adj}} {{connector}}").render(adj=vocab.get_ruin_connector_adj(),
                                                                  connector=vocab.get_ruin_connector())
        self.description = a_or_an.a_or_an(self.description) + " " + self.description
