class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        opt = [None] * (len(cost) + 1)

        opt[-1] = 0
        opt[-2] = cost[-1]

        for i in range(len(cost) - 2, -1, -1):
            opt[i] = cost[i] + min(opt[i+1], opt[i+2])
        
        return min(opt[0], opt[1])        