# Pseudocode for DFS on a grid
grid = [[]] # some 2D array

def DFS(exploredNodes, x, y):
    if not (0 <= y < len(grid)):
        return

    if not (0 <= x < len(grid[0])):
        return

    if (x, y) in exploredNodes:
        return 
    
    DFS(exploredNodes, x+1, y)
    DFS(exploredNodes, x-1, y)
    DFS(exploredNodes, x, y+1)
    DFS(exploredNodes, x, y-1)

DFS(set(), 0, 0)