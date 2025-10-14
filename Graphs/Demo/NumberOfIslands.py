# We can approach this through any graph search algorithm
# I will provide a DFS solution because it's the most straight forward
# However BFS will work too

# This also uses a standard implementation of DFS with a set
# Can you think of a way to solve this problem w/o using a set?

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        exploredNodes = set()
        m = len(grid)
        n = len(grid[0])

        numIslands = 0

        def DFS(explored, x, y):
            if not (0 <= x < n):
                return

            if not (0 <= y < m):
                return
            
            if (x,y) in explored:
                return

            if grid[y][x] == "0":
                return

            explored.add((x,y))
            
            DFS(explored, x+1, y)
            DFS(explored, x-1, y)
            DFS(explored, x, y+1)
            DFS(explored, x, y-1)
        
        for y in range(m):
            for x in range(n):
                if (x,y) in exploredNodes:
                    continue
                
                if grid[y][x] == "0":
                    continue
                
                DFS(exploredNodes, x, y)
                numIslands += 1
        
        return numIslands