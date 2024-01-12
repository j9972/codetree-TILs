import heapq

n = int(input())
arr = list(map(int,input().split()))

heap = []

for i in arr:
    heapq.heappush(heap, i)

    if len(heap) < 3:
        print(-1)
    else:
        f = heapq.heappop(heap)
        s = heapq.heappop(heap)
        t = heapq.heappop(heap)

        print(f*s*t)
        heapq.heappush(heap, f)
        heapq.heappush(heap, s)
        heapq.heappush(heap, t)