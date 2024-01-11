import heapq

n = int(input())
heap = []

for _ in range(n):
    data = list(input().split())
    heapq.heapify(heap)

    if data[0] == 'push':
        heapq.heappush(heap, -int(data[1]))

    elif data[0] == 'size':
        print(len(heap))

    elif data[0] == 'empty':
        if len(heap) == 0:
            print(1)
        else:
            print(0)

    elif data[0] == 'pop':
        print(-heapq.heappop(heap))

    elif data[0] == 'top':
        print(heap[-1])