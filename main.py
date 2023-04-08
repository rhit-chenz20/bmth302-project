from transitive import assemble_reads
from transitive import plot_transitive_orientation

adj_mat = [[0, 1, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0],]

def convert(a):
    adjList = []
    for i in range(len(a)):
        li = [i,]
        for j in range(len(a[i])):
            if a[i][j] != 0:
                li.append(j)
        adjList.append(' '.join(str(x) for x in li))
    return adjList

# assemble_reads(convert(adj_mat))
plot_transitive_orientation(convert(adj_mat))