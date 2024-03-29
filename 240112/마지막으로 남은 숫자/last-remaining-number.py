import heapq

n = int(input())

arr = list(map(int,input().split()))

heap = []
for i in arr:
    heapq.heappush(heap, -i)

while True:
    if not heap or len(heap) == 1:
        break

    val1 = -heapq.heappop(heap)
    val2 = -heapq.heappop(heap)

    if (val1-val2) == 0:
        continue
    else:
        heapq.heappush(heap, -(val1-val2))

if not heap:
    print(-1)
else:
    print(-heapq.heappop(heap))