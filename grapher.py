import networkx as nx
from matplotlib import pyplot
from freezeword import md_writer

def save_graph(ruin, name="out.png"):
    G=nx.Graph()
    G.add_node("outside".title(), posxy=[0, -1])
    for room in ruin.rooms:
        G.add_node(room.full_name.title(), posxy=room.pos)
    for room in ruin.rooms:
        for key, val in room.connections.items():
            if val is None:
                pass
            elif val == 'entrance':
                G.add_edge(room.full_name.title(), "outside".title())
            else:
                connected_room = val[1]
                G.add_edge(room.full_name.title(), connected_room.full_name.title())

    positions = nx.get_node_attributes(G,'posxy')
    pyplot.figure(1,figsize=(8,8))
    pyplot.title("Map of " + ruin.name.title())
    nx.draw(G, positions, node_size=2000, node_color=(0, .7, .8), edge_color='#00aaaa', width=4, linewidths=0.2, with_labels=False, transparent=True)
    for p in positions:  # raise text positions
        v_offset = positions[p][0] % 4
        positions[p][1] += [0.14, -0.07, .07, -0.14][v_offset]
    nx.draw_networkx_labels(G, positions, font_size=10)
    pyplot.savefig(md_writer.output_folder+"/images/" + name, transparent=True) # save as png
    pyplot.close()

