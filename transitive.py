import networkx as nx
import matplotlib.pyplot as plt
from queues import Queue
from clique_orientation import get_final_orientation

# not transitive orientable
# G2 = nx.petersen_graph()

# transitive orientable graph
G2 = nx.cycle_graph(4)

def generate_transitive_orientation(G: nx.Graph):
    G3: nx.DiGraph = nx.create_empty_copy(G).to_directed()
    maxnode = sorted(G2.degree, key=lambda x: x[1], reverse=True)[0][0]
    i = _helper(G, maxnode, G3)
    return None if i == 1 else G3
    
def is_valid(G0: nx.DiGraph, nodes):
    neigh = nodes[0]
    succ = nodes[1]
    node = nodes[2]
    if (len (nx.induced_subgraph(G0, nodes).edges) == 3):
        try:
            nx.find_cycle(G0.subgraph(G0,[neigh, node, succ]))
            print("not comparability graph")
            return False
        except nx.NetworkXNoCycle:
            return True
    else:
        # no succ neigh edge 
        if ((((nodes[0], nodes[1]) in G0.edges()) and ((nodes[1], nodes[2]) in G0.edges()))
        or (((nodes[0], nodes[2]) in G0.edges()) and ((nodes[2], nodes[1]) in G0.edges()))
        or (((nodes[1], nodes[2]) in G0.edges()) and ((nodes[2], nodes[0]) in G0.edges()))
        or (((nodes[1], nodes[0]) in G0.edges()) and ((nodes[0], nodes[2]) in G0.edges()))
        or (((nodes[2], nodes[0]) in G0.edges()) and ((nodes[0], nodes[1]) in G0.edges()))
        or (((nodes[2], nodes[1]) in G0.edges()) and ((nodes[1], nodes[0]) in G0.edges()))):
            print("not comparability graph")
            return True

# G is the original graph; G0 is the result of transitive orientation
def _helper(G: nx.Graph, source, G0: nx.DiGraph):
    visited=[]    
    # keep visited nodes and enqueued nodes with their successors
    nodes_succ = {}
    # make source node
    next_nodes = Queue()
    for neigh in G.neighbors(source):
        G0.add_edge(source, neigh)
        for n in G.neighbors(neigh):
            if(n not in G.neighbors(source)):
                G0.add_edge(n, neigh)
            nodes_succ.update({n: [source]})

        next_nodes.enqueue(neigh)
        nodes_succ.update({source: []})
        visited.append(source)
    
    while (not next_nodes.is_empty()):
        node = next_nodes.dequeue()
        for neigh in G.neighbors(node):
            for succ in nodes_succ.get(node):
                if(succ == neigh):
                    continue
                else:
                    # triangle: succ node neigh
                    # check if every trangle satisfy the rule
                    if ((neigh, node) in G0.edges() or (node, neigh) in G0.edges()):
                        # has edges between node and neigh
                        if ((neigh, succ) in G0.edges() or (succ, neigh) in G0.edges()):
                            # has edges between neigh and succ
                            try:
                                nx.find_cycle(G0.subgraph(G0,[neigh, node, succ]))
                                print("not comparability graph")
                                return 1
                            except nx.NetworkXNoCycle:
                                continue
                        else:
                            # no succ neigh edge 
                            if ((((succ, node) in G0.edges()) and ((node, neigh) in G0.edges()))
                            or (((neigh, node) in G0.edges()) and ((node, succ) in G0.edges()))):
                                print("not comparability graph")
                                return
                    else:
                        # no edge has been assigned neigh and node
                        if ((neigh, succ) in G0.edges()):
                            # neigh->succ
                            if ((succ, node) in G0.edges()):
                                G0.add_edge(neigh, node)
                        elif ((succ, neigh) in G0.edges()):
                            # succ->neigh
                            if ((node, succ) in G0.edges()):
                                G0.add_edge(node, neigh)
                        else:
                            # no succ neigh edge 
                            if ((succ, node) in G0.edges()):
                                #   succ->node
                                G0.add_edge(neigh, node)
                            elif (node, succ) in G0.edges():
                                  G0.add_edge(node, neigh)

            if (neigh in nodes_succ.keys()):
                newlist = nodes_succ.get(neigh).append(node)
                nodes_succ.update({neigh, newlist})
            else:
                nodes_succ.update({neigh, [node]})
            next_nodes.enqueue(neigh) 
        visited.append(node)

    for (s1, s2) in G.edges():
        if ((s1, s2) not in G0.edges() and (s2, s1) not in G0.edges()):
            G0.add_edge(s1, s2)
            for succ in G.neighbors(s1):
                if(not is_valid(G0, [s1, s2, succ])):
                    break
            G0.remove_edge(s1,s2)
            G0.add_edge(s2, s1)
            for succ in G.neighbors(s2):
                if(not is_valid(G0, [s1, s2, succ])):
                    print("not comparability graph")
                    return 1

G3 = generate_transitive_orientation(G2)

if(not G3 ==  None):
    target = nx.transitive_reduction(G2)
    print(target)
    print(G3)
    print(G3.edges() == target.edges())
    get_final_orientation(G2, G3)

