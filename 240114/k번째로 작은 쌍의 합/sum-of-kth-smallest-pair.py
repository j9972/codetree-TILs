import heapq

n,m,k = map(int,input().split())

a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))

heap = []

for i in range(n):
    heapq.heappush(heap, (a[i] + b[0], i ,0))

for i in range(k-1):
    _,idx1, idx2 = heapq.heappop(heap)

    idx2 += 1
    if idx2 <= m:
        heapq.heappush(heap, (a[idx1] + b[idx2] , idx1, idx2))

print(heapq.heappop(heap)[0])