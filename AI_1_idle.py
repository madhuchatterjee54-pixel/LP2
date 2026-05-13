graph = {                                  # Dictionary representing the graph
    '5' : ['3','7'],                   # Node 5 is connected to 3 and 7
    '3' : ['2', '4'],                  # Node 3 is connected to 2 and 4
    '7' : ['8'],                       # Node 7 is connected to 8
    '2' : [],                          # Node 2 has no neighbours
    '4' : ['8'],                       # Node 4 is connected to 8
    '8' : []                           # Node 8 has no neighbours
}

# Breadth-First Search (BFS)

visited = []                           # List to store visited nodes
queue = []                             # Queue used for BFS traversal

def bfs(visited, graph, node):         # Function definition for BFS
    visited.append(node)               # Add starting node to visited list
    queue.append(node)                 # Add starting node to queue

    while queue:                       # Loop runs until queue becomes empty
        m = queue.pop(0)               # Remove first element from queue
        print(m, end="\n")             # Print current node

        for neighbour in graph[m]:     # Traverse all neighbours of current node
            if neighbour not in visited:   # Check if neighbour already visited
                visited.append(neighbour)  # Mark neighbour as visited
                queue.append(neighbour)    # Add neighbour to queue


# Depth-First Search (DFS)

visited1 = set()                       # Set to store visited nodes in DFS

def dfs(visited1, graph, node):        # Function definition for DFS
    if node not in visited1:           # Check if node is not visited
        print(node)                    # Print current node
        visited1.add(node)             # Add node to visited set

        for neighbour in graph[node]:  # Traverse neighbours of current node
            dfs(visited1, graph, neighbour) # Recursive DFS call


flag = 1                               # Variable used to control menu loop

while flag == 1:                       # Loop runs until user exits

    print("1. Breadth-First Search")
    print("2. Depth-First Search")
    print("3. Exit")

    ch = int(input("Enter your Choice (from 1 to 3) :"))  # Take user input

    if ch == 1:                        # If user selects BFS

        print("Following is the Breadth-First Search")

        visited.clear()                # Clear previous visited nodes
        queue.clear()                  # Clear previous queue data

        bfs(visited, graph, '5')       # Call BFS starting from node 5

        a = input("Do you want to continue (y/n) :")  # Ask user to continue

        if a == "y":                   # If user enters y
            flag = 1                   # Continue program
        else:
            flag = 0                   # Exit program
            print("Thanks for using this program!")

    elif ch == 2:                      # If user selects DFS

        print("Following is the Depth-First Search")

        visited1.clear()               # Clear previous DFS visited set

        dfs(visited1, graph, '5')      # Call DFS starting from node 5

        a = input("Do you want to continue (y/n) :")  # Ask user to continue

        if a == "y":                   # Continue program
            flag = 1
        else:
            flag = 0                   # Exit program
            print("Thanks for using this program!")

    elif ch == 3:                      # If user selects Exit

        flag = 0                       # Stop loop
        print("Thanks for using this program!")

    else:                              # If invalid choice entered

        print("!!Wrong Choice!!")

        a = input("Do you want to continue (y/n) :")

        if a == "y":
            flag = 1                   # Continue program
        else:
            flag = 0                   # Exit program
            print("Thanks for using this program!")
