# Pseudocode for DFS

def dfs(exploredNodes, node):
    if node in exploredNodes:
        return
    
    # we know "node" is unexplored - let's explore it now
    for neighbour in node.neighbours:
        dfs(neighbour)

dfs(set(), rootNode)