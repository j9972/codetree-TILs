import heapq

n = int(input())
arr = list(map(int,input().split()))

heap = []
sum_val = arr[n-1]
ans = 0
heapq.heappush(heap, arr[n-1])

for k in range(n-2,0,-1):
    heapq.heappush(heap, arr[k])
    sum_val += arr[k]

    val = heap[0]
    avg = (sum_val - val) / ( n - k - 1)

    if avg > ans:
        ans = avg

print("{:.2f}".format(ans))