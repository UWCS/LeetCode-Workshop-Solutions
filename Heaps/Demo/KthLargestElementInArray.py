import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ourHeap = []

        for num in nums:
            heapq.heappush(ourHeap, num)

            if len(ourHeap) > k:
                heapq.heappop(ourHeap)
        
        return ourHeap[0]