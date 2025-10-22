import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x,y in points:
            distSq = (x**2) + (y**2)
            heapq.heappush(maxHeap, ((-1 * distSq),( x, y)))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            
        # now we need to extract the points from maxHeap
        toReturn = list(map(lambda pair: pair[1], maxHeap))

        # we can also do this using a for loop
        # toReturn = []
        #
        # for pair in maxHeap:
        #     toReturn.append(pair[1]) # extract out the points
        
        return toReturn