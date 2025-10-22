import heapq

theList = [11, 6, 3, 1, 9] # unsorted
heapq.heapify(theList) # "heapify" is imported from heapq

print(theList) # now sorted! [1, 6, 3, 11, 9]

heapq.heappush(theList, 5)
print(theList) # [1, 6, 3, 11, 9, 5]

smallestElement = heapq.heappop(theList)
print(smallestElement) # 1
print(theList) # [3, 6, 5, 11, 9]

# looking at the smallest element (but not popping)
print(theList[0]) # 3