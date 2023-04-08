import networkx as nx
import matplotlib.pyplot as plt

def get_final_orientation(G2: nx.Graph, G3 : nx.DiGraph):
    cliques = nx.find_cliques(G2)
    hashable_c = []
    for c in cliques:
        t = nx.Graph()
        t.add_nodes_from(c)
        hashable_c.append(t)
    interval_graph = nx.DiGraph()
    interval_graph.add_nodes_from(hashable_c)
    generate_final_orientation(G3, interval_graph)
    final_answer = nx.algorithms.tournament.hamiltonian_path(interval_graph)
    print("Here's ordered cliques")
    for g in final_answer:
        print(g.nodes())

def generate_final_orientation(orientedG: nx.DiGraph, G0: nx.DiGraph):
    for clique in G0.nodes():
        for o_clique in G0.nodes():
            if(o_clique != clique and (clique, o_clique) not in G0.edges() and (o_clique, clique) not in G0.edges()):
                # for every pair of cliques, get difference
                diff_c = [x for x in clique.nodes() if x not in o_clique.nodes()]
                diff_o = [x for x in o_clique.nodes() if x not in clique.nodes()]
                # add the direction of the cliques based on the transitive orientation
                edge_to_add = (clique, o_clique) if (diff_c[0],diff_o[0]) in orientedG else (o_clique, clique)
                G0.add_edge(edge_to_add[0], edge_to_add[1])


def draw(G: nx.DiGraph):
    nx.draw_networkx(G)
    plt.show()
