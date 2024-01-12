import heapq

n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

heap = []

for i in arr:
    if i == 0:
        if len(heap) != 0:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -i)