class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOranges = 0

        currentRotters = set()
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    freshOranges += 1
                elif grid[y][x] == 2:
                    currentRotters.add((x,y))
        
        nextRotters = set()
        nGenerations = 0

        def explore(x, y, rotSet):
            nonlocal freshOranges

            if not (0 <= y < len(grid)):
                return
            
            if not (0 <= x < len(grid[0])):
                return
            
            if (x,y) in rotSet:
                return
            
            if grid[y][x] == 1:
                rotSet.add((x,y))
                grid[y][x] = 2
                freshOranges -= 1
        
        while currentRotters and (freshOranges > 0):
            for x,y in currentRotters:
                explore(x+1, y, nextRotters)
                explore(x-1, y, nextRotters)
                explore(x, y+1, nextRotters)
                explore(x, y-1, nextRotters)

            currentRotters = nextRotters
            nextRotters = set()

            nGenerations += 1

        if freshOranges > 0:
            return -1
        else:
            return nGenerations