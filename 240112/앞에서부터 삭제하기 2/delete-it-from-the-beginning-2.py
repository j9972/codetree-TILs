import heapq

n = int(input())
arr = list(map(int,input().split()))
ans = 0

for k in range(1,n-1):
    tmp = arr[k:]

    heapq.heapify(tmp)
    heapq.heappop(tmp)
    
    length = len(tmp)
    sum_val = 0
    while len(tmp) != 0:
        sum_val += heapq.heappop(tmp)
    
    ans = max(ans, round(sum_val / length, 2))
print("{:.2f}".format(ans))