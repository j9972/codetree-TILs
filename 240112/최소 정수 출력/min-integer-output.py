import heapq

pq = []

n = int(input())
for _ in range(n):
    val = int(input())

    if val == 0:
        if len(pq) != 0:
            print(heapq.heappop(pq))
        else:
            print(0)
    else:
        heapq.heappush(pq, val)