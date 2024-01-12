import heapq

arr = []

for _ in range(int(input())):
    m = int(input())
    arr = list(map(int, input().split()))
    
    max_heap, min_heap = [], []
    mid = arr[0]
    print(mid,end=' ')

    for i in range(1,m):
        # 짝수
        if i % 2 == 1:
            if mid > arr[i]:
                heapq.heappush(max_heap, -arr[i])
            else:
                heapq.heappush(min_heap, arr[i])    
        else:
            if len(max_heap) > len(min_heap):
                new = -heapq.heappop(max_heap)
            else:
                new = heapq.heappop(min_heap)
            
            num = sorted([new, arr[i], mid])

            heapq.heappush(max_heap, -num[0])
            mid = num[1]
            heapq.heappush(min_heap, num[2])

            print(mid,end=' ')
    print()