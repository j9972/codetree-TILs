import heapq

n = int(input())

arr = list(map(int,input().split()))

heap = []
for i in arr:
    heapq.heappush(heap, -i)

while len(heap) != 1:
    val1 = heapq.heappop(heap)
    val2 = heapq.heappop(heap)

    if abs(val1-val2) == 0:
        continue
    else:
        heapq.heappush(heap, -abs(val1-val2))

if not heap:
    print(0)
else:
    print(-heapq.heappop(heap))