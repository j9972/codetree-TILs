import sys

n = int(input())
OFFSET = 1000

arr = []
for i in range(n):
    x,y = map(int,input().split())
    arr.append([x+OFFSET,y+OFFSET])

ans = sys.maxsize

for i in range(1,n-1):
    dist = 0
    idx = 0
    for j in range(1,n):
        if i == j:
            continue
        dist += abs(arr[idx][0] - arr[j][0]) + abs(arr[idx][1] - arr[j][1])
        idx = j
    ans = min(ans, dist)
print(ans)