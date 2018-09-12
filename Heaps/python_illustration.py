import heapq

heap = []

heapq.heappush(heap, 5)  # set = {5}
heapq.heappush(heap, 2)  # set = {5, 2}
heapq.heappush(heap, 10) # set = {5, 2, 10}

heapq.heappop(heap) # result = 2. set = {5, 10}
heapq.heappop(heap) # result = 5. set = {10}

heapq.heappush(heap, 7)  # set = {10, 7}
heapq.heappush(heap, 12) # set = {10, 7, 12}

heapq.heappop(heap) # result = 7.  set = {10, 12}
heapq.heappop(heap) # result = 10. set = {12}

print(heap, type(heap))
