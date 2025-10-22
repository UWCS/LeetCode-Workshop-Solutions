import heapq

aHeap = []

heapq.heappush(aHeap, (5, "Some random data"))
heapq.heappush(aHeap, (2, "More random data"))
heapq.heappush(aHeap, (7, "Another piece of random data"))

print(aHeap) # it's ordered by the numbers (first element in the ())