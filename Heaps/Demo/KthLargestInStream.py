import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        self.minHeap = nums
        self.k = k

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) < self.k:
            return None
        elif len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # if len(heap) == self.k, then do nothing but return

        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)