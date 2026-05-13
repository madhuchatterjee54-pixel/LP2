# A* Algorithm in Python

# Heuristic values (estimated cost to reach goal)
heuristic = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0          # Goal node heuristic is always 0
}

# Graph with edge costs
graph = {
    'A': [('B', 2), ('E', 3)],   # A connected to B and E
    'B': [('C', 1), ('G', 9)],   # B connected to C and G
    'C': [],                     # C has no neighbours
    'D': [('G', 1)],             # D connected to G
    'E': [('D', 6)],             # E connected to D
    'G': []                      # Goal node
}

# Function for A* Search
def a_star(start, goal):

    open_list = [start]          # List of nodes to be checked
    closed_list = []             # List of visited nodes

    g = {}                       # Stores actual path cost
    g[start] = 0                 # Cost of start node is 0

    parent = {}                  # Dictionary to store parent nodes
    parent[start] = start

    while len(open_list) > 0:    # Loop until open list becomes empty

        n = None                 # Current node

        # Find node with minimum f(n) = g(n) + h(n)
        for v in open_list:

            if n == None or g[v] + heuristic[v] < g[n] + heuristic[n]:
                n = v

        # If node is not found
        if n == None:
            print("Path does not exist!")
            return

        # If goal node is reached
        if n == goal:

            path = []

            # Trace path from goal to start
            while parent[n] != n:
                path.append(n)
                n = parent[n]

            path.append(start)
            path.reverse()

            print("Path found:")
            print(path)

            return

        # Check neighbours of current node
        for (m, weight) in graph[n]:

            # If neighbour not visited
            if m not in open_list and m not in closed_list:

                open_list.append(m)       # Add neighbour to open list
                parent[m] = n            # Store parent
                g[m] = g[n] + weight     # Calculate path cost

            else:

                # If shorter path found
                if g[m] > g[n] + weight:

                    g[m] = g[n] + weight
                    parent[m] = n

                    # Move node back to open list
                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.append(m)

        open_list.remove(n)      # Remove current node from open list
        closed_list.append(n)    # Add current node to closed list

    print("Path does not exist!")


# Calling the function
a_star('A', 'G')
