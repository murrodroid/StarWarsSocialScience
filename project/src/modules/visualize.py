import netwulf as nw
import networkx as nx

def visualize(G):
    settings = {
        'node_color_model': 'group',
        'node_size': 10,
        'edge_width_factor': 0.3,
        'zoom_and_pan': True,
        'charge': -30,
        'link_distance': 30
    }
    nw.visualize(G, config=settings)