import heapq
import sys

n = int(input())

arr = []
for i in range(1,n+1):
    a,t = tuple(map(int,input().split()))
    arr.append((a, i, t))

#arr.append((sys.maxsize, n+1, 0))

arr.sort()

waiting = []
ans, exit_time = 0, 0

for a , idx, t in arr:
    while a >= exit_time and waiting:
        _, next_a, next_t = heapq.heappop(waiting)

        ans = max(ans, exit_time - next_a)

        exit_time += next_t


    if a >= exit_time:
        exit_time = a + t
    else:
        heapq.heappush(waiting, (idx, a, t))
print(ans)