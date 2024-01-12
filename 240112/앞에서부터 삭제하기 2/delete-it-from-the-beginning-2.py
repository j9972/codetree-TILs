import heapq

n = int(input())
arr = list(map(int,input().split()))
ans = 0

for k in range(1,n-1):
    tmp = arr[k:]

    heapq.heapify(tmp)
    heapq.heappop(tmp)
    
    ans = max(ans, sum(tmp) / len(tmp))
print("{:.2f}".format(ans))