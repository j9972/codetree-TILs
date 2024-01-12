import heapq
import sys

n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

ans = 0

heap = []
for i in arr:
    if i != 0:
        heapq.heappush(heap, (abs(i),i))
    else:  
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])