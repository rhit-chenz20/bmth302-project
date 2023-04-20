from transitive import assemble_reads
from transitive import plot_transitive_orientation

adj_mat = [[0, 1, 0, 0, 1, 0],
           [0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 1, 0],
           [0, 1, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0],]

plot_transitive_orientation(adj_mat)
assemble_reads(adj_mat)