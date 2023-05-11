from transitive import assemble_reads
from transitive import plot_transitive_orientation
from transitive import draw
import networkx

# not for demo
adj_mat = [[0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0],
            ]

# draw()
# plot_transitive_orientation(adj_mat)
# assemble_reads(adj_mat)