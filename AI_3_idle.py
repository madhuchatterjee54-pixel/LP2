# Prim's Minimum Spanning Tree (MST) Algorithm

INF = 9999999                         # Large value used as infinity

# Number of vertices in graph
N = 5

# Graph represented using adjacency matrix
# 0 means no connection between nodes
G = [
    [0, 19, 5, 0, 0],                # Connections of node 0
    [19, 0, 5, 9, 2],                # Connections of node 1
    [5, 5, 0, 1, 6],                 # Connections of node 2
    [0, 9, 1, 0, 1],                 # Connections of node 3
    [0, 2, 6, 1, 0]                  # Connections of node 4
]

# List to track selected vertices
# Initially all are False (0)
selected_node = [0, 0, 0, 0, 0]

# Variable to count number of edges selected
no_edge = 0

# Start from first node (node 0)
selected_node[0] = True

# Print heading
print("Edge : Weight\n")

# MST will always have (N-1) edges
while (no_edge < N - 1):

    minimum = INF                    # Assume minimum edge is infinity
    a = 0                            # Row index
    b = 0                            # Column index

    # Traverse through all vertices
    for m in range(N):

        # Check if current node already selected
        if selected_node[m]:

            # Check all adjacent nodes
            for n in range(N):

                # Condition:
                # 1. Node should not already be selected
                # 2. There should be an edge between nodes
                if ((not selected_node[n]) and G[m][n]):

                    # Select edge with minimum weight
                    if minimum > G[m][n]:

                        minimum = G[m][n]   # Update minimum weight
                        a = m               # Store source vertex
                        b = n               # Store destination vertex

    # Print selected edge and its weight
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))

    # Mark destination node as selected
    selected_node[b] = True

    # Increase edge count
    no_edge += 1
