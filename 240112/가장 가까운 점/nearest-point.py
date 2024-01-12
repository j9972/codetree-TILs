import heapq

n,m = map(int,input().split())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
pq = []

for x,y in arr:
    heapq.heappush(pq, (abs(x)+abs(y), x, y))
                         
for i in range(m):

    _,x,y = heapq.heappop(pq)

    heapq.heappush(pq,(abs(x+2) + abs(y+2), x+2, y+2))

ans = heapq.heappop(pq)

print(ans[1], ans[2])