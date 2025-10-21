import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -1 * x, stones))
        heapify(stones)
        maxHeap = stones

        while len(stones) >= 2:
            s1 = -1 * heapq.heappop(stones)
            s2 = -1 * heapq.heappop(stones)

            if s1 == s2:
                continue
            
            heapq.heappush(stones, -1 * (s1 - s2))
        
        if stones:
            return -1 * stones[0]
        else:
            return 0