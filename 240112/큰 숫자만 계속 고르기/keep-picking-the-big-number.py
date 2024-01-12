import heapq

n,m = map(int,input().split())
arr = list(map(int,input().split()))
pq = []

for elem in arr:
    heapq.heappush(pq, -elem) # priority queue에 넣어줍니다.

for i in range(m):
    data = heapq.heappop(pq)
    data = abs(data) - 1
    heapq.heappush(pq,-data)

print(-heapq.heappop(pq))