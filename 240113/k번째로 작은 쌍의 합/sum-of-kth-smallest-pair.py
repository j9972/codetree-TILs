import heapq

n,m,k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

heap = [] # 2개의 원소와 그 합을 넣기

a.sort()
b.sort()

heapq.heappush(heap, (a[0]+b[0], b[0] ,a[0]))

for i in range(1,n):
    heapq.heappush(heap, (a[i]+b[0], b[0] ,a[i]))

for i in range(1,m):
    heapq.heappush(heap, (a[0]+b[i], a[0], b[i]))

#print(heap)
ans = 0
for i in range(k):
    ans = heapq.heappop(heap)
print(ans[0])