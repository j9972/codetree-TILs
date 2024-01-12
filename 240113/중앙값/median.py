import heapq

arr = []

for _ in range(int(input())):
    m = int(input())
    arr = list(map(int, input().split()))
    
    max_pq, min_pq = [], []
    mid = arr[0]

    print(mid, end=" ")

    for i in range(1,m):
        if i % 2 == 1:
            if arr[i] < mid:
                heapq.heappush(max_pq, -arr[i])
            else:
                heapq.heappush(min_pq, arr[i])
        else:
            if len(max_pq) > len(min_pq):
                new = -heapq.heappop(max_pq)
            else:
                new = heapq.heappop(min_pq)

        
            nums = sorted([arr[i], mid, new])

            heapq.heappush(max_pq, -nums[0])
            mid = nums[1]
            heapq.heappush(min_pq, nums[2])

            print(mid, end=" ")
    print()