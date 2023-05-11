import sympy
from collections import deque
import networkx as nx
from Levenshtein import distance 
from itertools import product
import matplotlib.pyplot as plt
import time

def chromatic_polynomial(G: nx.Graph):
    x = sympy.Symbol("x")
    stack = deque()
    stack.append(nx.MultiGraph(G, contraction_idx=0))

    polynomial = 0
    while stack:
        G = stack.pop()
        edges = list(G.edges)
        if not edges:
            polynomial += (-1) ** G.graph["contraction_idx"] * x ** len(G)
        else:
            e = edges[0]
            C = nx.contracted_edge(G, e, self_loops=True)
            C.graph["contraction_idx"] = G.graph["contraction_idx"] + 1
            C.remove_edge(e[0], e[0])
            G.remove_edge(*e)
            stack.append(G)
            stack.append(C)
    return polynomial

def generate_mutation_graph(n:int):
    G = nx.Graph()
    nodes = [''.join([str(x) for x in p]) for p in product([0, 1], repeat=n)]
    G.add_nodes_from(nodes)
    for node in nodes:
        edges = map(lambda y: (node,y), filter(lambda x: distance(node,x)==1, nodes))
        G.add_edges_from(edges)
    return G

def draw_graph(G):
    nx.draw_networkx(G)
    plt.show()
   
   
    

x=sympy.Symbol("x")

G = generate_mutation_graph(2)
# start_time = time.time()
# chro_2 = chromatic_polynomial(G)
# print("chromatic polynomial generation of 2 loci takes: %s seconds ---" % (time.time() - start_time))
# chro_number = chro_2.subs(x,-1)
# print("chromatic polynomial of 2 loci: ",chro_2)
# print("number of acyclic orientation: ",chro_number)
# print("------------------------------------")

# print(len(G))
# draw_graph(G)
# G.remove_edge(*list(G.edges)[0])
# draw_graph(G)
print(G)

G = generate_mutation_graph(3)
# # start_time = time.time()
# # chro_3 = chromatic_polynomial(G)
# # print("chromatic polynomial generation of 3 loci takes: %s seconds ---" % (time.time() - start_time))
# # chro_number = chro_3.subs(x,-1)
# # print("chromatic polynomial of 3 loci: ",chro_3)
# # print("number of acyclic orientation: ",chro_number)
# # print("------------------------------------")
# print(len(G))
print(G)
G = generate_mutation_graph(4)
# start_time = time.time()
# chro_4 = chromatic_polynomial(G)
# print("chromatic polynomial generation of 4 loci takes: %s seconds ---" % (time.time() - start_time))
# chro_number = chro_4.subs(x,-1)
# print("chromatic polynomial of 4 loci: ",chro_4)
# print("number of acyclic orientation: ",chro_number)
print(G)