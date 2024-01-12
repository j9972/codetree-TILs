import heapq

T = int(input())

for _ in range(T):

    left_max_pq = []
    right_min_pq = []

    list_print = []
    length = int(input())
    list_vals = list(map(int, input().split()))

    mid = list_vals[0]
    list_print.append(list_vals[0])

    for i in range((len(list_vals)-1)//2):
        vals = [list_vals[2*i+1], list_vals[2*i+2]]
        cnt = 0
        for val in vals:
            if val < mid:
                cnt+=1
                heapq.heappush(left_max_pq, -val)
            else:
                heapq.heappush(right_min_pq, val)

        if cnt==0:
            heapq.heappush(left_max_pq, -mid)
            mid = heapq.heappop(right_min_pq)
        elif cnt ==2:
            heapq.heappush(right_min_pq, mid)
            mid = -heapq.heappop(left_max_pq)
        
        list_print.append(mid)
    
    print(*list_print)