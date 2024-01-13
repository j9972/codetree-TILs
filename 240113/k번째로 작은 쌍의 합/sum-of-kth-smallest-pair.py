import heapq

n,m,k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

heap = [] # 2개의 원소와 그 합을 넣기

a.sort()
b.sort()

for i in range(m):
    heapq.heappush(heap, (a[0] + b[i], 0, i))

for i in range(k-1):
    _, idx1, idx2 = heapq.heappop(heap)

    idx1 += 1 
    if idx1 <= n:
        heapq.heappush(heap, (a[idx1] + b[idx2], idx1, idx2))

print(heapq.heappop(heap)[0])